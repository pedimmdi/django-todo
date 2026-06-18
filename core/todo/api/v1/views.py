from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import TodoList, Task
from .serializers import TodoListSerializer, TaskReadSerializer, TaskWriteSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample
from django.contrib.auth.models import AnonymousUser


@extend_schema_view(
    list=extend_schema(
        tags=["Todo Lists"],
        summary="List todo lists",
        responses=TodoListSerializer(many=True)
    ),

    retrieve=extend_schema(
        tags=["Todo Lists"],
        summary="Retrieve todo list",
        responses=TodoListSerializer
    ),

    create=extend_schema(
        tags=["Todo Lists"],
        summary="Create todo list",
        request=TodoListSerializer,
        responses=TodoListSerializer,
        examples=[
            OpenApiExample(
                "Todo List Example",
                value={
                    "title": "Work Tasks"
                },
                request_only=True,
            ),
        ],
    ),

    update=extend_schema(
        tags=["Todo Lists"],
        summary="Update todo list",
        request=TodoListSerializer,
        responses=TodoListSerializer
    ),

    partial_update=extend_schema(
        tags=["Todo Lists"],
        summary="Partially update todo list",
        request=TodoListSerializer,
        responses=TodoListSerializer
    ),

    destroy=extend_schema(
        tags=["Todo Lists"],
        summary="Delete todo list"
    ),
)
class TodoListViewSet(viewsets.ModelViewSet):
    lookup_field = "pk"
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if (not hasattr(self, "request") or isinstance(self.request.user, AnonymousUser)):
            return TodoList.objects.none()
        return TodoList.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema_view(
    list=extend_schema(
        tags=["Tasks"],
        summary="List tasks",
        responses=TaskReadSerializer(many=True)
    ),

    retrieve=extend_schema(
        tags=["Tasks"],
        summary="Retrieve task",
        responses=TaskReadSerializer
    ),

    create=extend_schema(
        tags=["Tasks"],
        summary="Create task",
        request=TaskWriteSerializer,
        responses=TaskReadSerializer,
        examples=[
            OpenApiExample(
                "Task Example",
                value={
                    "title": "Learn Django",
                    "description": "Read DRF documentation",
                    "todo_list": 1,
                    "status": 1,
                    "priority": 2
                },
                request_only=True,
            ),
        ],
    ),

    update=extend_schema(
        tags=["Tasks"],
        summary="Update task",
        request=TaskWriteSerializer,
        responses=TaskReadSerializer
    ),

    partial_update=extend_schema(
        tags=["Tasks"],
        summary="Partially update task",
        request=TaskWriteSerializer,
        responses=TaskReadSerializer
    ),

    destroy=extend_schema(
        tags=["Tasks"],
        summary="Delete task"
    ),
)
class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if (not hasattr(self, "request") or isinstance(self.request.user, AnonymousUser)):
            return Task.objects.none()
        return Task.objects.select_related(
            "status", "priority", "todo_list",
        ).filter(todo_list__user=self.request.user)
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TaskReadSerializer
        return TaskWriteSerializer
