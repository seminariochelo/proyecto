from django.conf.urls import patterns, include, url
from control2.apps.blog.views import base,registro
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base),
    url(r'^registro/$', registro),
)
