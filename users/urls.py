from django.urls import path  # this line of code will link the path to an actual view
from .views import login_view, RegisterView  # views.py will be directed to this path
urlpatterns = [
    # creating a mapping between a path and a view with start with an entry (path)
    path('login/', login_view, name='login'),  # the path requires a string which will be the actual path, the name will reference the our route
    
    path('register/', RegisterView.as_view(),name = 'register')
]
