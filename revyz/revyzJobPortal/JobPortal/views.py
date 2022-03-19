# Create your views here.
from this import d
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *

from rest_framework import generics
from JobPortal.serializers import CandidateSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here : 
# function bases.
def home(request):
    if request.user.is_authenticated:
        candidates=Candidates.objects.filter(company__name=request.user.username)
        context={
            'candidates':candidates,
        }
        return render(request,'hr.html',context)
    else:
        companies=Company.objects.all()
        context={
            'companies':companies,
        }
        return render(request,'Jobseeker.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
       return render(request,'login.html')
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        Form=UserCreationForm()
        if request.method=='POST':
            Form=UserCreationForm(request.POST)
            if Form.is_valid():
                currUser=Form.save()
                Company.objects.create(user=currUser,name=currUser.username)
                return redirect('login')
        context={
            'form':Form
        }
        return render(request,'register.html',context)
def applyPage(request):
    form=ApplyForm()
    if request.method=='POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'apply.html',context)

#class bases
class API_objects(generics.ListCreateAPIView):
    
    queryset = Candidates.objects.all()    
    serializer_class = CandidateSerializer
    print("Get call")
    filter_fields = (        
        'city',
    )
    search_fields = (
        '^techskill',
    )

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Candidates.objects.all()     
    serializer_class = CandidateSerializer
    print("POST / PUT called")

