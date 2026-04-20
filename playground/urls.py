from django.urls import path
from . import views

#URL confiig

urlpatterns = [
        path('hello/',views.say_hello)
        ]

