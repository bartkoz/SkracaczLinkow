from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^link$', views.skrocone, name='skrocone'),
url(r'^(?P<short>\w+)$', views.link, name='follow'),
]
