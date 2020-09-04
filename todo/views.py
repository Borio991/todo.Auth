from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# home ------------------------------------------------------------------------------------------------


def home(request):
    return render(request, 'todo/home.html')

# auth ------------------------------------------------------------------------------------------------


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                error = 'this username is already taken'
                form = UserCreationForm()
                return render(request, 'todo/signupuser.html', {'form': form, 'error': error})
        else:
            error = 'passwords didnt match'
            form = UserCreationForm()
            return render(request, 'todo/signupuser.html', {'form': form, 'error': error})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'todo/loginuser.html', {'form': form})
    else:
        if request.method == 'POST':
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                error = 'username or password didnt match,try again'
                form = AuthenticationForm()
                return render(request, 'todo/loginuser.html', {'form': form, 'error': error})
            else:
                user.save()
                login(request, user)
                return redirect('currenttodo')

# Todo--------------------------------------------------------------------------------------------


def currenttodo(request):
    return render(request, 'todo/currenttodo.html')
