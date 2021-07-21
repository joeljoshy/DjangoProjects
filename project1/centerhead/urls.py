from django.urls import path
from .views import add_course,add_batch,review_batch


urlpatterns=[
    path('addcourse',add_course,name="addcourse"),
    path('addbatch',add_batch,name="addbatch"),
    path('review_batch',review_batch,name="batchreview")
]