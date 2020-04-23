from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^post/(?P<id>[0-9]+)$', views.detailsPost, name="details"),
]