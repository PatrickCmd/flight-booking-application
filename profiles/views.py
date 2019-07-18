from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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
            queryset =qs
        else:
            queryset = qs.filter(owner=self.request.user)
        return queryset
    
    def get_object(self):
        if not self.get_queryset():
            raise ValidationError("You have no profile yet")
        
        if self.request.user.is_admin or self.request.user == self.get_queryset().first().owner:
            try:
                obj = get_object_or_404(
                    self.get_queryset(), pk=self.kwargs.get('pk')
                )
                return obj
            except:
                raise PermissionDenied("profile not found.")
        raise PermissionDenied("Not allowed to view this profile.")
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
