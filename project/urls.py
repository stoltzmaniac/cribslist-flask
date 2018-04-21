# -*- coding:utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from dcf import views as core_views

admin.autodiscover()

urlpatterns = [
    # Authorization
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^user/', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('dcf.urls', namespace='dcf')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
