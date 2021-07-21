from django.urls import path
from .views import follow_ups,admissions

urlpatterns=[
    path('followups',follow_ups),
    path('admissions',admissions)
]