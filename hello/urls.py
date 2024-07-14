from django.urls import path
from hello import views

urlpatterns = [
  path("", views.home, name="home"),
  # path - defines a route "hello/" that accepts a variable string called 'name'
  # the string is passed to the 'views.hello_there' function specified in the second argument to 'path'
  # URL routes are case-sensitive, if you want /hello/<name> and /Hello/<name> - define paths for each
  path("hello/<name>", views.hello_there, name="hello_there"),
]