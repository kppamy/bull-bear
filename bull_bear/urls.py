from django.conf import urls
from django.contrib import admin

from . import views

urlpatterns = [
    urls.url(r'^$', views.index, name='index'),
    urls.url(r'^admin/', admin.site.urls),
]

