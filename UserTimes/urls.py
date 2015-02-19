__author__ = 'BhargavKumarReddy'
from django.conf.urls import patterns, url
from UserTimes.models import User123,TimeSheet123
from django.core.urlresolvers import reverse

from UserTimes import views

urlpatterns = patterns('', url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/create/$', views.TimeCreate.as_view(), name='createtime'),
                       url(r'^create/$', views.createuser.as_view(), name='createuser'),
                       url(r'^(?P<pk>\d+)/update/$', views.UserUpdate.as_view(), name='updateuser'),
                       url(r'^(?P<pk>\d+)/(?P<tpk>\d+)/updatetime/$', views.TimeSheetUpdate.as_view(),
                           name='sheetupdate'),
                       url(r'^(?P<pk>\d+)/delete/$', views.User_Delete.as_view(), name='deleteuser'),
                       url(r'^(?P<pk>\d+)/(?P<tpk>\d+)/deletetime/$', views.Time_Sheet_Delete.as_view(),
                           name='sheetdelete'),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'),
                       )