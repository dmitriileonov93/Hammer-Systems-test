from django.urls import path

from .views import APIMyProfile


urlpatterns = [
    path('my_profile/', APIMyProfile.as_view()),
]
