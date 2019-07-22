from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateView

app_name = "authenticate"

urlpatterns = [
    path("user/<pk>/", UserRetrieveUpdateView.as_view(), name="user-details"),
    path("users/", RegistrationAPIView.as_view(), name="create-list-users"),
    path("users/login/", LoginAPIView.as_view(), name="login"),
]
