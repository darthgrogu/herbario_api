from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from setup.permissions import GlobalDefaultPermission
from bosque_events.models import TreeEvent
from bosque_events.serializers import TreeEventSerializer


class TreeEventCreateListView(generics.ListCreateAPIView):
    serializer_class = TreeEventSerializer
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
    queryset = TreeEvent.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        tree_id = self.request.query_params.get('tree_id', None)
        if tree_id is not None:
            queryset = queryset.filter(tree__id=tree_id)
        return queryset


class TreeEventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreeEvent.objects.all()
    serializer_class = TreeEventSerializer
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
