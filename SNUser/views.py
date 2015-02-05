from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from SNUser.models import SNUser
from SNUser.forms import SNUserForm

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def new_user(request):
    registered = False
    if request.method == 'POST':
        user_form = SNUserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            login(request, user)
        else:
            print user_form.errors
    else:
        user_form = SNUserForm()
    return render(request, 'SNUser/new_user.html', {'user_form': user_form, 'registered': registered})
