from django.urls import path
from .views import addition

urlpatterns=[
    path('addition',addition)
]