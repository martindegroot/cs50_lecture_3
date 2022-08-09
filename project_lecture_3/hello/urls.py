from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("martin", views.martin, name="martin"),
    path("johan", views.johan, name="johan")
]