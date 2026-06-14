from django.db import models
from django.conf import settings


class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TodoList(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
