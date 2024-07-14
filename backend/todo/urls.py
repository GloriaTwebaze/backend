from django.urls import path

from .views import CreateTodo, ViewTodos

urlpatterns = [
    path("create-todo/", CreateTodo.as_view(), name="create"),
    path('view-todos/', ViewTodos.as_view(), name='view-todos')
]