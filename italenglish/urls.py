# The 2 patterns that really should not be in the list below are:
# 1. r'^$'
# 2. r'^profile$'
# They are included here anyway because the corresponding templates are defined
# in the wordapp_* folders.

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'italenglish.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'wordapp_3.views.home', name='home'),
    url(r'^translate/', include('wordapp_3.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'wordapp_3/login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'template_name': 'wordapp_3/logout.html'}),
    url(r'^profile$', 'wordapp_3.views.profile', name='profile'),
)
