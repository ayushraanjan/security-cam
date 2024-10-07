from django.urls import path
from . import views

urlpatterns = [
    path('check-event-status/', views.check_event_status, name='check_event_status'),
    path('trigger-event/', views.trigger_event, name='trigger_event'),
    path('reset-event-status/', views.reset_event_status, name='reset_event_status'),
    path('',views.index, name='index'),
    path('incident123/', views.static_page, name='static_page'),
]
