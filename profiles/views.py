from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader

from .models import PassportInfo
from .serializers import PassPortSerializer
from .renderers import PassportInfoRenderer


class PassportInfoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (PassportInfoRenderer,)
    serializer_class = PassPortSerializer

    def get_queryset(self):
        qs = PassportInfo.objects.all()
        if self.request.user.is_admin:
            queryset = qs
        else:
            queryset = qs.filter(owner=self.request.user)
        return queryset

    def get_object(self):
        if not self.get_queryset():
            raise ValidationError("You have no profile yet")

        if (
            self.request.user.is_admin or self.request.user == self.get_queryset().first().owner
        ):
            try:
                obj = get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))
                return obj
            except:  # noqa E722
                raise Http404("profile not found.")
        raise PermissionDenied("Not allowed to view this profile.")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PassportPhotoUploadView(APIView):
    parser_classes = (MultiPartParser, JSONParser)

    @staticmethod
    def post(request, pk):
        if request.FILES.get("passport_photo"):
            file = request.data.get("passport_photo")

            upload_data = cloudinary.uploader.upload(file)
            passport = PassportInfo.objects.get(pk=pk)
            passport.passport_photo = upload_data["secure_url"]
            passport.save()
            return Response(
                {
                    "profile": {
                        "status": "success",
                        "passport_photo_url": upload_data["secure_url"],
                        "photo_data": upload_data,
                    }
                },
                status=status.HTTP_201_CREATED,
            )
