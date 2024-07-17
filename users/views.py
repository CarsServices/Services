from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def login_view(request): # I'm going to create a function that will be responsible for rendering the login and handling the functionality
    return render(request, "basic/login.html")
