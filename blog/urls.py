# blog/urls.py
from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),

    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^cbv/new/$', views_cbv.post_new),
]
