from django.urls import path
from .views import UserRegistrationView,NotesListCreateView,TaskListCreateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns=[
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('notes/',NotesListCreateView.as_view(),name='notes'),

    path('jwt_login/',TokenObtainPairView.as_view()),
    path('task/',TaskListCreateView.as_view()),
    
 ]