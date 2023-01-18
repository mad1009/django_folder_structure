from django.urls import path
from .api_view import greeting

urlpatterns = [
    path("", greeting)
]
