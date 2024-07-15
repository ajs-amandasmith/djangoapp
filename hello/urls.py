from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
  queryset=LogMessage.objects.order_by("-log_date")[:5], # Limits the results to the five most recent
  context_object_name="message_list",
  template_name="hello/home.html",
)

urlpatterns = [
  path("", home_list_view, name="home"),
  path("about/", views.about, name="about"),
  path("contact", views.contact, name="contact"),
  path("log/", views.log_message, name="log"),
  # path - defines a route "hello/" that accepts a variable string called 'name'
  # the string is passed to the 'views.hello_there' function specified in the second argument to 'path'
  # URL routes are case-sensitive, if you want /hello/<name> and /Hello/<name> - define paths for each
  path("hello/<name>", views.hello_there, name="hello_there"),
]



urlpatterns += staticfiles_urlpatterns()