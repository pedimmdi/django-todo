from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import TodoList, Task
from .serializers import TodoListSerializer, TaskReadSerializer, TaskWriteSerializer


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Task.objects.select_related(
            "status", "priority", "todo_list",
        ).filter(todo_list__user=self.request.user)
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TaskReadSerializer
        return TaskWriteSerializer
