from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from haystack.management.commands import update_index
from django.http import HttpResponse
from SNUser.models import SNUser
from SNUser.forms import SNUserForm, ChangeBioForm, ChangePasswordForm
from Posts.models import Post
from Posts.forms import PostForm


def index(request):
    return render(request, 'index.html', {})


def new_user(request):
    if request.method == 'POST':
        user_form = SNUserForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = SNUser.objects.create_user(**user_form.cleaned_data)
            update_index.Command().handle()
            login(request, user)
            return redirect('home_page')
        else:
            print user_form.errors
    else:
        user_form = SNUserForm()
    return render(request, 'SNUser/new_user.html', {'user_form': user_form, })


def login_page(request):
    if request.user.is_authenticated():
        return redirect('home_page')
    next_page = request.GET.get('next', 'home_page')
    if request.method == 'POST':
        auth_form = AuthenticationForm(request, data=request.POST)
        if auth_form.is_valid():
            login(request, auth_form.get_user())
            return redirect(next_page)
    else:
        auth_form = AuthenticationForm(request)
    return render(request, 'SNUser/login.html', {'form': auth_form, 'next': next_page})


@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login_page')
def home_page(request):
    post_form = PostForm()
    posts = request.user.post_set.all().order_by('-time')
    return render(request, 'SNUser/home.html', {'form': post_form, 'posts': posts})


@login_required(login_url='login_page')
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


@login_required(login_url='login_page')
def create_post(request):
    user = request.user
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.owner = user
            new_post.save()
            return render(request, "Posts/post_template.html", {"post": new_post})
    return redirect('home_page')


@login_required(login_url='login_page')
def settings(request):
    user = request.user
    if request.method == 'POST':
        password = request.POST.get('password')
        if user.check_password(password):
            logout(request)
            user.delete()
            return redirect('index')
    return render(request, 'SNUser/settings.html', {})


def profile(request, user_id):
    if not user_id:
        if request.user.is_authenticated():
            return redirect('home_page')
        else:
            return redirect('index')
    user = SNUser.objects.filter(pk=user_id)
    if not user:
        return redirect('home_page')
    post_list = user[0].post_set.all().order_by('-time')
    return render(request, 'SNUser/profile.html', {'owner': user[0], 'posts': post_list})


@login_required(login_url='login_page')
def change_bio(request):
    if request.method == 'POST':
        bio = ChangeBioForm(request.POST)
        if bio.is_valid():
            request.user.bio = bio.cleaned_data.get('bio')
            request.user.save()
            return redirect('home_page')
    curr_bio = request.user.bio
    bio_form = ChangeBioForm(initial={'bio': curr_bio})
    return render(request, 'SNUser/change_bio.html', {'form': bio_form})


@login_required(login_url='login_page')
def change_password(request):
    if request.method == 'POST':
        passwords = ChangePasswordForm(request.POST)
        if passwords.is_valid():
            new_password = passwords.cleaned_data.get('password')
            old_password = passwords.cleaned_data.get('old_password')
            if request.user.check_password(old_password):
                user = request.user
                user.set_password(new_password)
                user.save()
                return redirect('home_page')
    pass_form = ChangePasswordForm()
    return render(request, 'SNUser/change_password.html', {'form': pass_form})
