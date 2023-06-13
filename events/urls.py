from django.urls import path
from django.contrib.auth.decorators import login_required

from events import views

urlpatterns = [
    path('<int:year>/<str:month>/', views.home),
    path('venue/<venue_id>', views.show_venue, name="show-venue"),
    path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
    path('update_event/<event_id>', views.update_event, name="update-event"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),
    path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
    path('venue_csv', views.venue_csv, name='venue-csv'),
    path('venue_pdf', views.venue_pdf, name='venue-pdf'),
    path('', views.home, name='home'),
    path('events', views.all_events, name="list-events"),
    path('add_venue', login_required(views.add_venue), name="add-venue"),
    path('add_event', login_required(views.add_event), name="add-event"),
    path('list_venue', views.list_venue, name="list-venue"),
    path('search_venues', views.search_venues, name="search-venues"),
]
