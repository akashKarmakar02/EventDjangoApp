from django.contrib import admin
from django.urls import path, include
from allauth.account.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('accounts', include('allauth.urls'))
]

admin.site.site_header = "My Club Administration Page"
admin.site.site_title = "My Club Administration Page"
admin.site.index_title = ""
