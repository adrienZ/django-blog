from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^category/(?P<category_label>[A-Za-z]+)/$', views.category, name='category'),
    url(r'^login/$', auth_views.login, name='login',  kwargs={'redirect_authenticated_user': True}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/../posts/'},  name='logout'),
    url(r'^write/$', views.WriteView,  name='write'),
]