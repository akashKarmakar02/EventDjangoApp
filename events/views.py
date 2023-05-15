import csv

from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Generate a PDF File
def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

    text_obj = c.beginText()
    text_obj.setTextOrigin(inch, inch)
    text_obj.setFont("Helvetica", 14)

    venues = Venue.objects.all()

    for venue in venues:
        text_obj.textLine(f'Venue Name: {venue.name}')
        text_obj.textLine(f'Address: {venue.address}')
        text_obj.textLine(f'Zip Code: {venue.zip_code}')
        text_obj.textLine(f'Phone: {venue.phone}')
        text_obj.textLine(f'Website: {venue.web}')
        text_obj.textLine(f'Email: {venue.email_address}')
        text_obj.textLine('')
        text_obj.textLine('')

    c.drawText(text_obj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')


# Generate a CSV file
def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venue.csv'

    writer = csv.writer(response)

    venues = Venue.objects.all()

    writer.writerow(['Venue', 'Address', 'Zip Code', 'Phone', 'Website', 'Email Address'])
    for venue in venues:
        writer.writerow([venue, venue.address, venue.zip_code, venue.phone, venue.web, venue.email_address])

    return response


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
    event_list = Event.objects.all().order_by('name')

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


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})


def list_venue(request):
    venue_list = Venue.objects.all().order_by('name')
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


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/events')

    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()

    return HttpResponseRedirect('/events')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()

    return HttpResponseRedirect('/list_venue')
