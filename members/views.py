from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib import messages
from .forms import RegisterUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list-events')
        else:
            messages.error(request, message="There Was An Error Logging In, Try Again...")
            return redirect('login-user')

    return render(request, 'authentication/login.html')


def logout_user(request):
    if request.method == "GET":
        a = get_user(request)
        if a.is_authenticated:
            logout(request)
        return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        errors = []
        for error_field in form.errors.values():
            for error in error_field:
                errors.append(error)

        if form.is_valid():
            form.save()
            username = form.clean_username()
            password = form.clean_password2()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registered Successfully!!")
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, "authentication/register_user.html", {'form': form})
