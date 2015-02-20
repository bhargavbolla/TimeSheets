__author__ = 'BhargavKumarReddy'

from django.utils.translation import gettext_lazy as _
from django import forms
from UserTimes.models import User123, TimeSheet123
import datetime
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from UserTimes.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User123
        fields = ('user_name', 'position', 'hours_needed')


class TimeSheetform(forms.ModelForm):
    class Meta:
        model = TimeSheet123


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile