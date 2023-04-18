from django.contrib import admin
from .models import MyClubUser, Event, Venue

admin.site.register(MyClubUser)
admin.site.register(Venue)
admin.site.register(Event)
