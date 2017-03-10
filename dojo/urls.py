# dojo/urls.py
from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),

    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),

    url(r'^list1/$', views.post_list1),
    url(r'^list2/$', views.post_list2),
    url(r'^list3/$', views.post_list3),
    url(r'^excel/$', views.excel_download),

    url(r'^cbv/list1/$', views_cbv.post_list1),
    url(r'^cbv/list2/$', views_cbv.post_list2),
    # url(r'^cbv/list3/$', views_cbv.post_list3),
    # url(r'^cbv/excel/$', views_cbv.excel_download),
]
