from django.db import models
from django.contrib.auth.models import User


class MyClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email', max_length=120)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=30)
    phone = models.IntegerField('Phone no', blank=True)
    web = models.URLField('Web Site', blank=True)
    email_address = models.EmailField('Email Address', max_length=120, blank=True)
    owner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
