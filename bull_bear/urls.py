from django.conf import urls
from django.contrib import admin

from . import views

urlpatterns = [
    urls.url(r'^$', views.index, name='index'),
    urls.url(r'^event/(?P<event_id>[0-9]+)/$', views.event, name='event'),
    urls.url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    urls.url(r'^admin/', admin.site.urls),
]

