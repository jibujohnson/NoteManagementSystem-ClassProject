from django.contrib.auth.models import User
from rest_framework import serializers
from .models import NoteDb,TaskDb

class RegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','password']

    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=NoteDb
        fields='__all__'
        read_only_fields=['id','user','created_date']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskDb
        fields='__all__'
        read_only_fields=['id','user','created_date'] 