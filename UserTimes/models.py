from django.db import models
from django.contrib.auth.models import User


class User123(models.Model):
    user_name = models.OneToOneField(User)
    position = models.CharField(max_length=200)
    hours_needed = models.PositiveIntegerField(default=80)

    def __unicode__(self):
        return self.user_name


class TimeSheet123(models.Model):
    user = models.ForeignKey(User123)
    date_worked = models.DateField(default="2014-02-02")
    time_from = models.TimeField(default="10:15:20")
    time_to = models.TimeField(default="10:15:20")
    time_total = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __unicode__(self):
        return str(self.time_total)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username