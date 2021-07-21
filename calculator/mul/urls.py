from django.urls import path
from .views import multiplication

urlpatterns=[
    path('multiplication',multiplication)
]