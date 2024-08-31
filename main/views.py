# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def main_view(request):
    # return HttpResponse("<h1>Welcome to AutoCarView!") #we use this when we import httpResponse

    return render(request, "basic/index.html", {"name": "Skimmer Wheel"})
@login_required
def home_view(request):
    return render(request, "basic/home.html")
