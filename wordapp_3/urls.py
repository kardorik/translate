from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^show_list$', views.show_list, name='show_list'),
    url(r'^profile$', views.profile, name='profile'),
]
