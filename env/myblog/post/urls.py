from django.conf.urls import include, url
from django.contrib import admin

from .views import (
        post_list,
        post_create,
        post_detail,
        post_update,
        post_delete,
        form_create,
)
urlpatterns = [
    url(r'^$', post_list),
    url(r'create/$', post_create),
    url(r'detail/(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    url(r'form/$', form_create),
]
