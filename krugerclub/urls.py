"""krugerclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtail_admin_urls
from wagtail.documents import urls as wagtail_document_urls

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),

    path('cms/', include(wagtail_admin_urls)),
    path('document/', include(wagtail_document_urls)),
    path('blog/', include('blog.urls', namespace="blog")),
    path('', include(wagtail_urls))
]
