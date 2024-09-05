from django.urls import path
from .views import MemoryCreateView, MemoryListView, MemoryUpdateView, MemoryDeleteView, memory

urlpatterns = [
    path('create/', MemoryCreateView.as_view(), name='memory-create'),
    path('memory/', memory, name='memory'),
    path('memory-list/', MemoryListView.as_view(), name='memory-list'),
    path('memory/update/<int:pk>/', MemoryUpdateView.as_view(), name='memory-update'),
    path('memory/delete/<int:pk>/', MemoryDeleteView.as_view(), name='memory-delete'),
]

