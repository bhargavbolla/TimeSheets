__author__ = 'BhargavKumarReddy'

from django.utils.translation import gettext_lazy as _
from django import forms
from UserTimes.models import User123, TimeSheet123
import datetime
from django.utils import timezone

class UserForm(forms.ModelForm):
    class Meta:
        model = User123
        fields = ('user_name', 'position', 'hours_needed')


class TimeSheetform(forms.ModelForm):
    class Meta:
        model = TimeSheet123