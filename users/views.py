from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from django.http import HttpResponse

# Create your views here.

def login_view(request): # I'm going to create a function that will be responsible for rendering the login and handling the functionality
    
    if request.method == 'POST':   #If the  request method is set to post that means the user has to input some details into the server
        login_form = AuthenticationForm(request = request,data= request.POST) # this will create a form which will have information passed by client to the server, so basically the post will store the information
        user = None
        if login_form.is_valid():  #validating if the user name and the pass word is correct then we are set to log in for the post method
            username =login_form.cleaned_data.get('username')
            password= login_form.cleaned_data.get('password')
            user= authenticate(username = username, password = password) # this will create a user which will contain the username and the password of the user
            print(user) #this will print a user when  the login is successful
        
        if user is not None: # if the sign in is successful AND NOT EMPTY then i ll pass this to another page say homepage
            login(request, user) #then we can login the user with his credentials and provide his username
            messages.success(request, f'Successfully logged in as {username}') #welcome message that will be displaying
            return redirect('home')   #redirecting the user to the home page after loggingin
        else:  #else maybe the user should input the correct credentials or create a new account
            pass  #if the sign in isnot  successful  then we will thell the user to login again
    elif request.method=='GET':     #If the  request method is set to get that means we create an instance of authentication form with nothing in it 
        login_form = AuthenticationForm() #setting the login_form so that it can have te AuthenticationForm passed through it
    return render(request, "basic/login.html", {'login_form':login_form})
