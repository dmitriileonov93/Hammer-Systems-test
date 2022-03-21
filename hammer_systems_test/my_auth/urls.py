from django.urls import path

from .views import APIPhoneToCode, APICodeToToken

urlpatterns = [
    path('phone/', APIPhoneToCode.as_view()),
    path('token/', APICodeToToken.as_view()),
]
