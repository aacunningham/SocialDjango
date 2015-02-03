from django.conf.urls import patterns, url
from userProfile import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new_user/$', views.new_user, name='new_user'),
)
