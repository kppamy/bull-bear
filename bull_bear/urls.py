from django.conf import urls
from django.contrib import admin

from . import views

urlpatterns = [
    urls.url(r'^$', views.index, name='index'),
    urls.url(r'^gamble/(?P<gamble_id>[0-9]+)/$', views.gamble, name='gamble'),
    urls.url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    urls.url(r'^admin/', admin.site.urls),
]

