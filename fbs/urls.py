"""fbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views import generic

from rest_framework.response import Response
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

# coreapi documentation
schema_view = get_schema_view(title="FBS Platform API", permission_classes=[])

urlpatterns = [
    path('', generic.RedirectView.as_view(url='/docs', permanent=False)),
    path('admin/', admin.site.urls),
    path('fbs-api/', include('authenticate.urls', namespace='authenticate')),
    path('fbs-api/', include('profiles.urls', namespace='profiles')),
    path('fbs-api/', include('flight.urls', namespace='flights')),

    # documentation urls
    path('docs', include_docs_urls(title='FBS Platform API', permission_classes=[])),
    path('schema', schema_view),
]
