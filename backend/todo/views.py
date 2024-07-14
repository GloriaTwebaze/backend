from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from rest_framework import generics, status
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response

class CreateTodo(generics.CreateAPIView):
    serializer_class = TodoSerializer
    def perform_create(self, serailizer):
        serailizer.save()
    
    def create(self, request, *args, **kwargs):
        serailizer = self.get_serializer(data=request.data)
        serailizer.is_valid(raise_exception=True)
        self.perform_create(serailizer)
        headers = self.get_success_headers(serailizer.data)
        return Response(serailizer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class ViewTodos(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all()


class EditTodo(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        try:
            todo = self.get_object()
            self.perform_destroy(todo)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)