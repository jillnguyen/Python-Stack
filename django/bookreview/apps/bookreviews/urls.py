from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^add$', views.add),
    url(r'^addpage$', views.addpage),
    url(r'^bookpage/(?P<book_id>\d+)$', views.bookpage),
    url(r'^addreview/(?P<book_id>\d+)$', views.addreview),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^logout$', views.logout),
]