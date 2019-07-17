from django.urls import path

from .views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateView,
    AccountVerifyAPIView
)

app_name = 'authenticate'

urlpatterns = [
    path('user/', UserRetrieveUpdateView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/verify_account/<token>',
         AccountVerifyAPIView.as_view(), name='verify_account'),
]
