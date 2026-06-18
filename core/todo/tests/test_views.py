from rest_framework import status
from todo.tests.base import BaseAPITestCase
from todo.models import TodoList, Task


class TodoListViewTest(BaseAPITestCase):
    def test_create_todolist(self):
        self.authenticate()
        payload = {"title": "My List"}
        response = self.client.post("/api/v1/todo/todo-lists/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_list_todolists(self):
        self.authenticate()
        TodoList.objects.create(title="List1", user=self.user)
        response = self.client.get("/api/v1/todo/todo-lists/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_user_cannot_see_other_users_lists(self):
        self.authenticate()
        TodoList.objects.create(title="Mine", user=self.user)
        TodoList.objects.create(title="Not Mine", user=self.other_user)
        response = self.client.get("/api/v1/todo/todo-lists/")
        self.assertEqual(len(response.data), 1)


class TaskViewTest(BaseAPITestCase):
    def test_create_task(self):
        self.authenticate()
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        payload = {"title": "Learn Django", "todo_list": todo_list.id, "status": self.status.id, "priority": self.priority.id}
        response = self.client.post("/api/v1/todo/tasks/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_tasks_returns_nested_data(self):
        self.authenticate()
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        Task.objects.create(title="Learn DRF", todo_list=todo_list, status=self.status, priority=self.priority)
        response = self.client.get("/api/v1/todo/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("name", response.data[0]["status"])
        
    def test_user_cannot_create_task_in_other_users_list(self):
        self.authenticate()
        other_list = TodoList.objects.create(title="Other List", user=self.other_user)
        payload = {"title": "Hack", "todo_list": other_list.id, "status": self.status.id, "priority": self.priority.id}
        response = self.client.post("/api/v1/todo/tasks/", payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_task(self):
        self.authenticate()
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        task = Task.objects.create(title="Learn Django", todo_list=todo_list, status=self.status, priority=self.priority)
        response = self.client.get(f"/api/v1/todo/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Learn Django")

    def test_update_task(self):
        self.authenticate()
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        task = Task.objects.create(title="Old Title", todo_list=todo_list, status=self.status, priority=self.priority)
        payload = {"title": "New Title", "todo_list": todo_list.id, "status": self.status.id, "priority": self.priority.id}
        response = self.client.put(f"/api/v1/todo/tasks/{task.id}/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "New Title")
    
    def test_delete_task(self):
        self.authenticate()
        todo_list = TodoList.objects.create(title="My List", user=self.user)
        task = Task.objects.create(title="Delete Me", todo_list=todo_list, status=self.status, priority=self.priority)
        response = self.client.delete(f"/api/v1/todo/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
    
    def test_user_cannot_retrieve_other_users_task(self):
        self.authenticate()
        other_list = TodoList.objects.create(title="Other List", user=self.other_user)
        task = Task.objects.create(title="Secret Task", todo_list=other_list, status=self.status, priority=self.priority)
        response = self.client.get(f"/api/v1/todo/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_update_other_users_task(self):
        self.authenticate()
        other_list = TodoList.objects.create(title="Other List", user=self.other_user)
        task = Task.objects.create(title="Secret Task", todo_list=other_list, status=self.status, priority=self.priority)
        payload = {"title": "Hack", "todo_list": other_list.id, "status": self.status.id, "priority": self.priority.id}
        response = self.client.put(f"/api/v1/todo/tasks/{task.id}/", payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_delete_other_users_task(self):
        self.authenticate()
        other_list = TodoList.objects.create(title="Other List", user=self.other_user)
        task = Task.objects.create(title="Secret Task", todo_list=other_list, status=self.status, priority=self.priority)
        response = self.client.delete(f"/api/v1/todo/tasks/{task.id}/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthenticated_user_cannot_access_tasks(self):
        response = self.client.get("/api/v1/todo/tasks/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_empty_task_list(self):
        self.authenticate()
        response = self.client.get("/api/v1/todo/tasks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
