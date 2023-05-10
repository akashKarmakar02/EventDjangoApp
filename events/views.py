from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm
from django.http import HttpResponseRedirect


# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(theyear=year, themonth=month_number, withyear=True)

    return render(request, 'events/home.html', {
        "name": "Akash",
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal
    })


def all_events(request):
    event_list = Event.objects.all()

    return render(request, 'events/event_list.html', {"event_list": event_list})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def list_venue(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', {'list': venue_list})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})


def search_venues(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venue.html', {'searched': searched, 'venues': venues})
    else:
        return HttpResponseRedirect('/')


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/list_venue')
    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})
