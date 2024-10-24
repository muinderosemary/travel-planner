from django.urls import path
from .views import home, login

urlpatterns = [
    path('', view=home),
    path('sign-in', view=login),
]
