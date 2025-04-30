from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from setup.permissions import GlobalDefaultPermission
from bosque_trees.models import Tree
from bosque_trees.serializers import TreeSerializer


class TreeCreateListView(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]


class TreeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    permission_classes = [IsAuthenticated, GlobalDefaultPermission]
