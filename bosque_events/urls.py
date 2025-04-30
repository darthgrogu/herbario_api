from django.urls import path
from bosque_events.views import TreeEventCreateListView, TreeEventRetrieveUpdateDestroyView

urlpatterns = [
    path('bosque/events/', TreeEventCreateListView.as_view(), name='event-list-create'),
    path('bosque/events/<int:pk>/', TreeEventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
]
