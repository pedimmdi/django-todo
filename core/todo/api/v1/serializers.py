from rest_framework import serializers
from todo.models import Status, Priority, TodoList, Task
from django.contrib.auth.models import AnonymousUser


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name"]


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = ["id", "name"]


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["id", "title", "user"]
        extra_kwargs = {
            'user': {'read_only': True}
        }


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "todo_list", "status", "priority", "deadline", "created_at", "updated_at"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            self.fields["todo_list"].queryset = TodoList.objects.filter(user=request.user)
        else:
            self.fields["todo_list"].queryset = TodoList.objects.none()


class TaskReadSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    priority = PrioritySerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = ["id", "title", "description", "todo_list", "status", "priority", "deadline", "created_at", "updated_at"]
