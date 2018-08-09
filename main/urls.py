from django.urls import path
from . import views

urlpatterns = [
    path('<str:current_page_name>/', views.page, name='page'),
]
