from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PassportInfoViewSet, PassportPhotoUploadView


router = DefaultRouter()
router.register(r'profiles', PassportInfoViewSet, base_name='profiles')


app_name = 'profiles'

urlpatterns = [
    path('profiles/<pk>/upload_passport_photo', PassportPhotoUploadView.as_view(),
         name='upload_passport_photo'),
]
urlpatterns += router.urls
