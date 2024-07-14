from django.urls import path

from .views import CreateTodo, ViewTodos, EditTodo, DeleteTodo

urlpatterns = [
    path("create-todo/", CreateTodo.as_view(), name="create"),
    path('view-todos/', ViewTodos.as_view(), name='view-todos'),
    path('edit-todo/', EditTodo.as_view(), name="edit-view"),
    path('delete/', DeleteTodo.as_view(), name="delete")
]