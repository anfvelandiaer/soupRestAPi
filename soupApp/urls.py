from django.conf.urls import url
from soupApp import views
from soupApp import api

urlpatterns = [
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^api/v1/create_user/$', api.UserCreate.as_view(), name="api_create_user"),
    url(r'^api/v1/login_user/$', api.Login.as_view(), name="api_create_user"),
    url(r'^api/v1/create_table/$', api.TableCreate.as_view(), name="api_create_table"),
    url(r'^api/v1/tables/$', api.TableList.as_view(), name="api_get_tables"),
    url(r'^api/v1/table/(?P<pk>[0-9]+)/$', api.TableDetail, name="api_get_table"),
]
