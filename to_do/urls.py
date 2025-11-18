from django.urls import path
from . import views
from .views import history

urlpatterns = [
  
  # Adding the task
  path('add_task/', views.add_task, name='add_task'),
  
  # Marked the task as completed, button click feature
  
  path('mark_as_done/ <int:pk>/', views.mark_as_done, name='mark_as_done'),
  
  
  # Mark the task as incomplete, button click feature
  path('mark_as_undone/ <int:pk>/', views.mark_as_undone, name='mark_as_undone'),
  
  # Edit the task, button click feature
  path('edit_task/ <int:pk>/', views.edit_task, name='edit_task'),
  
  # Delete the task, button feature
  path('delete_task/ <int:pk>/', views.delete_task, name='delete_task'),
  
]
