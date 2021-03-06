from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import viewsets

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^phrases/$', views.phrase_list),
    url(r'^phrases/(?P<pk>[0-9]+)/$', views.phrase_detail),
    url(r'^photos/$', views.photo_list),
    url(r'^photos/(?P<pk>[0-9]+)/$', views.photo_detail),
    url(r'^$', views.index)
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
