from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoListViewSet, TaskViewSet

router = DefaultRouter()
router.register(r"todo-lists", TodoListViewSet, basename="todo-list")
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("", include(router.urls))
]
