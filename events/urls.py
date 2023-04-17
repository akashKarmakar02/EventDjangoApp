from django.urls import path

from events import views

urlpatterns = [
    path('<int:year>/<str:month>/', views.home),
    path('', views.home),
]
