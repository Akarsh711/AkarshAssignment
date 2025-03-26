from django.urls import path
from .views import create_task, assign_task, get_tasks_for_user

urlpatterns = [
    path('create-tasks/', create_task, name='create_task'),
    path('assign-tasks/', assign_task, name='assign_task'),
    path('get-tasks-of-user/<int:user_id>', get_tasks_for_user, name='get_tasks_for_user'),
]
