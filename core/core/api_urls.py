from django.urls import path, include

urlpatterns = [
    path('v1/accounts/', include('accounts.api.v1.urls')),
    path('v1/todo/', include('todo.api.v1.urls'))
]
