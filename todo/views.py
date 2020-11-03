from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password

from .models import Todo
from .forms import TodoForm, LoginForm
from .forms import RegisterForm


# Create your views here.
def index(request):

    todo = Todo.objects.filter(user=request.user)

    form = TodoForm()

    context = {'todo': todo, 'form': form}
    return render(request, 'index.html', context)


def register_page(request):
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@require_POST
def add_task(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_task = Todo(text=request.POST['text'], user=request.user)
        new_task.save()

    return redirect('index')


def complete_task(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.complete = True
    task.delete()
    return redirect('index')


def register_user(request):
    form = RegisterForm(require_POST)

    try:
        user = User.objects.get(username=request.POST['email'])
        form = RegisterForm()
        context = {'form': form,
                   'error': 'The username you entered has already been taken. Please try another username.'}
        return render(request, 'register.html', context)
    except User.DoesNotExist:
        user = User(username=request.POST['email'])
        user.set_password(request.POST['password'])
        user.save()

    login(request, user)
    return redirect('index')


def log_in(request):
    form = LoginForm(require_POST)

    try:
        user = User.objects.get(username=request.POST['email'])
        curr_password = user.password
        if check_password(request.POST['password'], curr_password):
            login(request, user)
            return redirect('index')
        else:
            form = LoginForm()
            context = {'form': form,
                       'error': 'Not correct password'}
            return render(request, 'login.html', context)

    except User.DoesNotExist:
        form = LoginForm()
        context = {'form': form,
                   'error': 'The username you entered is not exist'}
        return render(request, 'login.html', context)


def log_out_user(request):
    logout(request)
    return redirect('login')
