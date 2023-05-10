from django.urls import path

from events import views

urlpatterns = [
    path('<int:year>/<str:month>/', views.home),
    path('venue/<venue_id>', views.show_venue, name="show-venue"),
    path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
    path('', views.home, name='home'),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name="add-venue"),
    path('add_event', views.add_event, name="add-event"),
    path('list_venue', views.list_venue, name="list-venue"),
    path('search_venues', views.search_venues, name="search-venues"),
]
