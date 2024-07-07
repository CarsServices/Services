# from django.http import HttpResponse
from django.shortcuts import render
def main_view(request):
    # return HttpResponse("<h1>Welcome to AutoCarView!") #we use this when we import httpResponse

    return render(request, "basic/index.html")
