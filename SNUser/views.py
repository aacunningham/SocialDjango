from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from SNUser.models import SNUser
from SNUser.forms import SNUserForm, SNUserLoginForm
from Posts.models import Post
from Posts.forms import PostForm

# Create your views here.

def index(request):
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
    return render(request, 'index.html', {'user_form': user_form, 'registered': registered})

def new_user(request):
    if request.method == 'POST':
        user_form = SNUserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            login(request, user)
        else:
            print user_form.errors
    else:
        user_form = SNUserForm()
    return render(request, 'SNUser/new_user.html', {'user_form': user_form,})

def login_page(request):
    if request.user.is_authenticated():
        return redirect('home_page')
    if request.method == 'POST':
        auth_form = AuthenticationForm(request, data=request.POST)
        if auth_form.is_valid():
            login(request, auth_form.get_user())
            return redirect('home_page')
    else:
        auth_form = AuthenticationForm(request)
    return render(request, 'SNUser/login.html', {'form': auth_form,})

@login_required
def logout_page(request):
    logout(request)
    return redirect('index')

@login_required
def home_page(request):
    user = request.user
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.owner = user
            new_post.save()
    post_form = PostForm()
    posts = user.post_set.all().order_by('-time')
    return render(request, 'SNUser/home.html', {'form': post_form, 'posts': posts})


def delete_post(request):
    user = request.user
    if request.method == 'GET':
        post_id = request.GET.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        if post.owner != user:
            return redirect('home_page')
        post.delete()
    response = "success"
    if not user.post_set.all():
        response = "<p>There are no posts related to yours.</p>"
    return HttpResponse(response)
