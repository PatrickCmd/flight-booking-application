from django.urls import path

from .views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateView,
    AccountVerifyAPIView
)

app_name = 'authenticate'

urlpatterns = [
    path('user/', UserRetrieveUpdateView.as_view(), name='user-details'),
    path('users/', RegistrationAPIView.as_view(), name='create-list-users'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('users/verify_account/<token>',
         AccountVerifyAPIView.as_view(), name='verify_account'),
]
