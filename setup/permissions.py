from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        model_name = view.queryset.model._meta.model_name
        app_label = view.queryset.model._meta.app_label
        action = self.__get_action_sufix(method)
        print(f'{app_label}.{action}_{model_name}')
        return f'{app_label}.{action}_{model_name}'

    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
