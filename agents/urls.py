from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register/(?P<backend>[^/]+)/$', views.API.as_view({'get': 'register'})),
    url(r'register_device$', views.API.as_view({'get': 'register_device'})),
    url(r'location$', views.API.as_view({'get': 'location', 'post': 'location'})),
    url(r'base_location$', views.API.as_view({'get': 'base_location'})),
]