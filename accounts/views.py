"""
This module defines the views for the 'accounts' application.

Functions:
    login(request): Handles user login.

Dependencies:
    django.shortcuts.render: Renders a template.
    django.shortcuts.redirect: Redirects to a different URL.
    django.contrib.auth.models.User: Represents a user in the authentication system.
    django.contrib.auth.models.auth: Provides authentication-related functions.
    django.contrib.messages: Provides a way to store messages in one request and retrieve them in a subsequent request.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    """
    Handles user login.

    If the request method is POST, it authenticates the user with the provided username and password.
    If authentication is successful, logs the user in and redirects to the home page.
    If authentication fails, displays an error message and redirects to the login page.
    If the request method is not POST, renders the login page.

    Args:
        request (HttpRequest): The request object used to generate this response.

    Returns:
        HttpResponse: The response object containing the rendered login page or a redirect.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print("Username taken")
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email taken")
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print("user created")
                messages.info(request,'User Created')
                return redirect('login')

        else:
            print('password is incorrect')
            messages.info(request,'Incorrect password')
            return redirect('register')

        return redirect('/')

    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')