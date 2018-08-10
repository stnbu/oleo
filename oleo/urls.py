from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/main/favicon.ico')),
    path('', RedirectView.as_view(url='/pages/home/')),
    path('pages/', include('main.urls')),
    path('admin/', admin.site.urls),
]
