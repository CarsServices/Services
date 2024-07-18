from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse

# Create your views here.

def login_view(request): # I'm going to create a function that will be responsible for rendering the login and handling the functionality
    
    if request.method == 'POST':   #If the  request method is set to post that means the user has to input some details into the server
        pass
    elif request.method=='GET':     #If the  request method is set to get that means we create an instance of authentication form with nothing in it 
        login_form = AuthenticationForm() #setting the login_form so that it can have te AuthenticationForm passed through it
    return render(request, "basic/login.html", {'login_form':login_form})
