from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
    
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
    
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user