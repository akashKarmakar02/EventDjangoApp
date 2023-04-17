from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


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
