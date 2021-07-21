from django.urls import path
from .views import subtraction

urlpatterns=[
    path('subtraction',subtraction)
]