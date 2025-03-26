from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Task
from .serializers import TaskSerializer, UserSerializer

User = get_user_model()

"""
    Create Task
"""
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    Assign task to particular users
"""
@api_view(['POST'])
def assign_task(request):
    task_id = request.data.get('task_id')
    user_ids = request.data.get('user_ids')
    try:
        task = Task.objects.get(id=task_id)
        users = User.objects.filter(id__in=user_ids)
        task.assigned_users.set(users)
        task.save()
        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


"""
    Retrieve tasks assigned to a specific user,
    but only show the current user in the assigned_users field
"""
@api_view(['GET'])
def get_tasks_for_user(request, user_id):

    # Ensure the user exists
    user = get_object_or_404(User, id=user_id)

    # Filter tasks assigned to the current user
    tasks = Task.objects.filter(assigned_users=user)

    # Prepare the filtered data
    data = []
    for task in tasks:
        serializer = TaskSerializer(task)
        task_data = serializer.data

        # Only include the current user in the assigned_users field
        task_data['assigned_users'] = [
            user for user in task_data['assigned_users'] if user['id'] == request.user.id
        ]

        data.append(task_data)

    return Response(data, status=status.HTTP_200_OK)
