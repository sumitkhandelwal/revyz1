from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from JobPortal import views

urlpatterns = [
    path('',home,name='home'), # function base
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('register/',registerUser,name='register'),
    path('apply/',applyPage,name='apply'),    
    path('basic/', views.API_objects.as_view()),  # class base
    path('basic/<int:pk>/', views.API_objects_details.as_view()),    
]

urlpatterns = format_suffix_patterns(urlpatterns)