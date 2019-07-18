from rest_framework.routers import DefaultRouter

from .views import PassportInfoViewSet


router = DefaultRouter()
router.register(r'profiles', PassportInfoViewSet, base_name='profiles')


app_name = 'profiles'
urlpatterns = router.urls
