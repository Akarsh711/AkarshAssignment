from django.db import models
from django.contrib.auth.models import User, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .manager import UserManager

"""
    Custom user to add phone number field
"""
class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(blank=True, null=True, region='IN')
    objects = UserManager()

    class Meta:
        # Explicitly set the model manager
        swappable = 'AUTH_USER_MODEL'
        verbose_name = "User"
        verbose_name_plural = "Users" 

    def __str__(self):
        return self.username


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_type = models.CharField(max_length=50, choices=[('urgent', 'Urgent'), ('normal', 'Normal')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    assigned_users = models.ManyToManyField(CustomUser, related_name='tasks')

    def __str__(self):
        return self.name