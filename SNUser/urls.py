from django.conf.urls import patterns, url
from SNUser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^post/delete/?$', views.delete_post, name='delete_post'),
)
