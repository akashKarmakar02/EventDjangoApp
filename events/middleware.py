from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class ProtectedViewMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        protected_urls = ["/add_venue", "/add_event", "/update_event"]

        if not request.user.is_authenticated:
            for path in protected_urls:
                if request.path.startswith(path):
                    messages.warning(request, 'Please log in to access this page.')
                    return redirect(reverse('login-user'))

        return response
