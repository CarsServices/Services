from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

# Create your views here.

def login_view(request): 
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Hello {username}')
                return redirect('home')
            else:
                messages.error(request, 'An error occurred trying to log you in. Please check your username or password.')
        else:
            messages.error(request, 'An error occurred trying to log you in. Please check your username or password.')
    else:
        login_form = AuthenticationForm()
    
    return render(request, "basics/login.html", {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        # pass
        register_form = UserCreationForm()
        return render(request, 'basic/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(request=request, data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            password = register_form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=password)
            login(request, user) 
            messages.success(
                request, f'User {user.username} registered successfully.')
            return redirect('home')
        



