from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from userProfile.models import UserProfile

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def new_user(request):
    return HttpResponse("New User!!")
