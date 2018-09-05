from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/main/favicon.ico')),
    path('resume/', RedirectView.as_view(url='/static/main/bin/resume-mike-burr.html')),
    path('', RedirectView.as_view(url='/pages/home/')),
    path('pages/', include('main.urls')),
]

# completely disable admin UI in production
if settings.DEBUG:
    urlpatterns.append(path('admin/', admin.site.urls))
