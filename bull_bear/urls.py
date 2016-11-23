from django.conf import urls
from django.contrib import admin

from . import views

urlpatterns = [
	urls.url('^', urls.include('django.contrib.auth.urls')),
  urls.url(r'^$', views.index, name='index'),
  urls.url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event'),
  urls.url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
  urls.url(r'^make_prediction/', views.make_prediction),
  urls.url(r'^admin/', admin.site.urls),
]

