__author__ = 'BhargavKumarReddy'
from django.conf.urls import patterns, url
from UserTimes.models import User123,TimeSheet123
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from UserTimes import views

urlpatterns = patterns('', url(r'^$', login_required(views.IndexView.as_view()),
                               name='index'),
                       url(r'^(?P<pk>\d+)/$', login_required(views.DetailView.as_view()), name='detail'),
                       url(r'^(?P<pk>\d+)/create/$', login_required(views.TimeCreate.as_view()), name='createtime'),
                       url(r'^create/$', login_required(views.createuser.as_view()), name='createuser'),
                       url(r'^(?P<pk>\d+)/update/$', login_required(views.UserUpdate.as_view()), name='updateuser'),
                       url(r'^(?P<pk>\d+)/(?P<tpk>\d+)/updatetime/$', login_required(views.TimeSheetUpdate.as_view()),
                           name='sheetupdate'),
                       url(r'^(?P<pk>\d+)/delete/$', login_required(views.User_Delete.as_view()), name='deleteuser'),
                       url(r'^(?P<pk>\d+)/(?P<tpk>\d+)/deletetime/$', login_required(views.Time_Sheet_Delete.as_view()),
                           name='sheetdelete'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'registration/login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^register/$', views.UserCreate.as_view(), name='register'),
                       )