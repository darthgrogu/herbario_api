from django.urls import path
from bosque_trees.views import TreeCreateListView, TreeRetrieveUpdateDestroyView

urlpatterns = [
    path('bosque/trees/', TreeCreateListView.as_view(), name='tree-list-create'),
    path('bosque/trees/<int:pk>/', TreeRetrieveUpdateDestroyView.as_view(), name='tree-detail'),
]
