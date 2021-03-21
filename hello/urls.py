from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("philipp", views.philipp, name="philipp"),
    path("<str:name>", views.greet, name="greet")
]