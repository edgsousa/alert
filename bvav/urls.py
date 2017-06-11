"""bvav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import api.views
import agents.views

router = DefaultRouter()
router.register('server', api.views.ServerStatus, base_name='server')
router.register('agents', agents.views.API, base_name='agents')

urlpatterns = [
    url(r'^app/',
        include([
            url(r'^admin/', admin.site.urls),
            url(r'^api/', include(router.urls)),
            url(r'', include('social_django.urls', namespace='social')),
            url(r'^', include('bvavsmsalert.urls'))
        ])),
]
