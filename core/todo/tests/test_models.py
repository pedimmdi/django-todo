from django.test import TestCase
from accounts.models import User
from todo.models import Status, Priority, TodoList, Task


class TodoModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="password123")
        self.status = Status.objects.create(name="To Do")
        self.priority = Priority.objects.create(name="High")

    def test_status_str(self):
        self.assertEqual(str(self.status), "To Do")

    def test_priority_str(self):
        self.assertEqual(str(self.priority), "High")

    def test_todolist_str(self):
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        self.assertEqual(str(todo_list), "My List")

    def test_task_str(self):
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        task = Task.objects.create(title="Learn DRF", todo_list=todo_list, status=self.status, priority=self.priority)
        self.assertEqual(str(task), "Learn DRF")
