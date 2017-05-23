from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView



urlpatterns = [
    #automatic redirect to /polls:index
    url(r'^$', RedirectView.as_view(url='posts/', permanent=False)),
    
    url(r'^posts/', include('posts.urls')),
    url(r'^admin/', admin.site.urls),
]