from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from UserTimes.models import User123, TimeSheet123
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm, TimeSheetform
import datetime
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


class UserCreate(generic.CreateView):
    model = User
    template_name = 'UserTimes/createuser.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('UserTimes:index'))

"""simple way to check if logged in  or not is by checking request.user.is_authenticated()"""


# @login_required(login_url='/login')
def login_page(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # redirect to success page!
        else:
            """ Here goes disabled account page """

    else:
        """ here invalid login error message set that variable here??"""


def logout_view(request):
    logout(request)
    # here goes a success page.


class IndexView(generic.ListView):
    template_name = 'UserTimes/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        try:
            return User123.objects.get(user_name=get_user(self.request))
        except ObjectDoesNotExist:
            return ""


class DetailView(generic.DetailView):
    model = User123
    template_name = 'UserTimes/detail.html'
    context_object_name = 'user1'


class createuser(generic.CreateView):
    model = User123
    template_name = 'UserTimes/createuser.html'
    form = UserForm
    fields = ('position', 'hours_needed')

    def form_valid(self, form):
        user_name = get_user(self.request)
        form.instance.user_name = user_name
        obj = form.save(commit=False)
        try:
            obj.save()
        except IntegrityError:
            return HttpResponse("It seems you already have created your <b>username:</b> "+user_name.username+" to log time, please use it!"
                                + "<a href= "+reverse('UserTimes:index')+"> click here to go back <a/>")

        return HttpResponseRedirect(reverse('UserTimes:detail', kwargs={'pk': obj.pk}))






class TimeCreate(CreateView):
    model = TimeSheet123
    template_name = 'UserTimes/createtime.html'
    fields = ['date_worked', 'time_from', 'time_to']

    def form_valid(self,form):
        user = self.kwargs.get('pk')
        form.instance.user = User123.objects.get(pk=user)
        #fmt = '%H:%M:%S'
        xer = (datetime.datetime.combine(form.instance.date_worked, form.instance.time_to)) - (datetime.datetime.combine(form.instance.date_worked, form.instance.time_from))
        xer = xer.total_seconds()

        form.instance.time_total = float(xer)/3600

        #tdelta = datetime.datetime.strptime(form.instance.time_to, fmt) - datetime.datetime.strptime(form.instance.time_form, fmt)
        #form.instance.time.total = (tdelta.seconds() / 3600)
        obj = form.save(commit=False)
        #obj.author = self.request.user
        obj.save()
        #return super(TimeCreate, self).form_valid(form)
        return HttpResponseRedirect(reverse('UserTimes:detail', kwargs={'pk': obj.user.pk}))

    """  def get_form_class(self):
        form_class = super(TimeCreate, self).get_form_class()
        user_pk=self.kwargs.get('pk')
        user_field = form_class.base_fields['user']
        user_field.initial = user_pk
        return form_class"""


class UserUpdate(UpdateView):
    model = User123
    fields = ['user_name', 'position', 'hours_needed']
    template_name = 'UserTimes/createuser.html'

    def form_valid(self, form):
        user = self.kwargs.get('pk')
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('UserTimes:detail', kwargs={'pk': obj.pk}))


class TimeSheetUpdate(UpdateView):
    model = TimeSheet123
    template_name = 'UserTimes/createtime.html'
    fields = ['date_worked', 'time_from', 'time_to']

    def form_valid(self,form):
        user = self.kwargs.get('tpk')
        form.instance.user = User123.objects.get(pk=user)
        xer = (datetime.datetime.combine(form.instance.date_worked, form.instance.time_to)) - (datetime.datetime.combine(form.instance.date_worked, form.instance.time_from))
        xer = xer.total_seconds()
        form.instance.time_total = float(xer)/3600
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('UserTimes:detail', kwargs={'pk': obj.user.pk}))


class User_Delete(DeleteView):
    model = User123
    template_name = 'UserTimes/deleteuser.html'
    context_object_name = 'userdelete'
    success_url = reverse_lazy('UserTimes:index')


class Time_Sheet_Delete(DeleteView):
    model = TimeSheet123
    context_object_name = 'timesheetdel'
    template_name = 'UserTimes/deletetime.html'

    def get_success_url(self):
        obj = self.kwargs.get('tpk')
        return reverse('UserTimes:detail', kwargs={'pk': obj})


""" def get_context_data(self, **kwargs):
        obj = self.kwargs.get('pk')"""

"""def delete(self, request, *args, **kwargs):
        obj = self.kwargs.get('pk')
     #   q = TimeSheets.objects.get(pk = obj)
        return HttpResponseRedirect(reverse('TimeSheet:detail', kwargs={'pk': obj}))

def get_context_object_name(self, obj):
        obj = self.kwargs.get('pk')
        timesheetdel = TimeSheets.objects.get(pk=obj)
        self.context_object_name = 'timesheetdel'"""





# if form.is_valid():
    #    save_it = form.save(commit=False)
     #   save_it.save()

   # return render_to_response("TimeSheets/createtime.html", locals(), context_instance=RequestContext(request))



#def detail(request, user_id):
 #   q = User.objects.get(pk=user_id)
  #  return HttpResponse("you're looking at Mr. %s." % q.user_name)

# Create your views here.
