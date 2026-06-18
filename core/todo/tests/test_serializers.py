from django.test import TestCase
from accounts.models import User
from todo.models import Status, Priority, TodoList, Task
from todo.api.v1.serializers import TodoListSerializer, TaskWriteSerializer, TaskReadSerializer


class TodoSerializersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="password123")
        self.status = Status.objects.create(name="To Do")
        self.priority = Priority.objects.create(name="High")
        self.todo_list = TodoList.objects.create(title="My List", user=self.user)
        
    def test_todolist_serializer(self):
        serializer = TodoListSerializer(self.todo_list)
        self.assertEqual(serializer.data["title"], "My List")
        
    def test_task_write_serializer(self):
        payload = {"title": "Learn Django", "todo_list": self.todo_list.id, "status": self.status.id, "priority": self.priority.id}
        serializer = TaskWriteSerializer(data=payload)
        self.assertTrue(serializer.is_valid())
        
    def test_task_read_serializer(self):
        task = Task.objects.create(title="Learn DRF", todo_list=self.todo_list, status=self.status, priority=self.priority)
        serializer = TaskReadSerializer(task)
        self.assertEqual(serializer.data["status"]["name"], "To Do")
        self.assertEqual(serializer.data["priority"]["name"], "High")
