# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from django.contrib import admin
from django.contrib.staticfiles.urls import static

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/admin'}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
