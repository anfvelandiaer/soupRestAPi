from django.conf.urls import url
from soupApp import api

urlpatterns = [
    url(r'^api/v1/create_user/$', api.UserCreate.as_view(), name="api_create_user"),
    url(r'^api/v1/login_user/$', api.Login.as_view(), name="api_create_user"),
    url(r'^api/v1/create_table/$', api.TableCreate.as_view(), name="api_create_table"),
    url(r'^api/v1/tables/$', api.TableList.as_view(), name="api_get_tables"),
    url(r'^api/v1/table/(?P<pk>[0-9]+)/$', api.TableDetail, name="api_get_table"),
    url(r'^api/v1/get_user/(?P<pk>[a-z0-9_-]+)/$', api.UserByToken, name="api_get_user"),
    url(r'^api/v1/save_game/$', api.GameCreate.as_view(), name="api_save_game"),
    url(r'^api/v1/games/$', api.GameList.as_view(), name="api_get_games"),
]
