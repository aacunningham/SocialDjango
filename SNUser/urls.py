from django.conf.urls import patterns, url
from SNUser import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^profile/(?P<user_id>[0-9]*)/?$', views.profile, name='profile'),
    url(r'^change-bio/$', views.change_bio, name='change_bio'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^post/delete/?$', views.delete_post, name='delete_post'),
    url(r'^post/create/?$', views.create_post, name='create_post'),
)
