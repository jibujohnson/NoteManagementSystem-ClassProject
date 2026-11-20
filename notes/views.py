from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import RegistrationSerializer,NotesSerializer,TaskSerializer
from .models import NoteDb,TaskDb
from rest_framework.permissions import IsAuthenticated

# Create your views here. 

class UserRegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class NotesListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        notes=NoteDb.objects.filter(user=request.user)
        serializer=NotesSerializer(notes,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                data=serializer.data
            )
        return Response(
            data=serializer.errors
        )

# class NoteRetrieveUpdateDeleteView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request,note_id):
#         note_object=get_object_or_404(NoteDb,id=note_id)
#         if note_object.user==request.user:
#             serializer=NotesSerializer(note_object)
#             return Response(data=serializer.data,status=status.HTTP_200_OK)
#         return Response(data={
#             "Warning":"You are not allowed to access this note."
#         },status=status.HTTP_403_FORBIDDEN)

class TaskListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        task=TaskDb.objects.filter(user=request.user)
        serializer=TaskSerializer(task,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(data=serializer.errors)

class TaskRetrieveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticated]
    def get_task(self,request,pk):
        return get_object_or_404(TaskDb,id=pk,user=request.user)
    
    # Read Single Task
    def get(self,request,id):
        task=self.get_task(request,id)
        serializer=TaskSerializer(task)
        return Response(serializer.data)


   