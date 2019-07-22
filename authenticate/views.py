from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authenticate.models import User
from authenticate.serializers import (
    RegistrationSerializer,
    LoginSerializer,
    UserSerializer,
)
from authenticate.renderers import UserJSONRenderer


class RegistrationAPIView(APIView):
    """Register a user to the platform"""

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        # sendEmailVerification(request, user, user_data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    """Login a registered user"""

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    """
    retrieve: fetch a user's details.
    update: Modif a user's details.
    """

    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer
    lookup_field = "pk"

    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


# class AccountVerifyAPIView(APIView, JWTAuthentication):
#     """
#     user email: Send verification link to the user email
#     """

#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserSerializer

#     def get(self, request, token):
#         try:
#             user, user_token = self.authenticate_credentials(request, token)
#             if not user.is_verified:
#                 user.is_verified = True
#                 user.save()
#                 return redirect(f"http://{request.get_host()}/fbs-api/users/login")
#             return Response(
#                 {
#                     "message": f"Go to login http://{request.get_host()}/fbs-api/users/login"
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         except:
#             raise serializers.ValidationError("Activation link invalid or expired")
