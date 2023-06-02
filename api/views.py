from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NotesSerializer,RegisterSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt import authentication
from django.contrib.auth.models import User

from rest_framework.pagination import LimitOffsetPagination


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    pagination_class = LimitOffsetPagination
    
    def  get_queryset(self):
        obj = Note.objects.filter(user=self.request.user)
        return obj
    
    def create(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        print(request)
        return super().destroy(request, *args, **kwargs)
    
    

class RegisterViewSet(viewsets.ModelViewSet):
    
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
 