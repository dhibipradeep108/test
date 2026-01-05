from django.urls import path
from . import views

urlpatterns = [
    path('tz/', views.set_timezone, name = 'set_timezone'),
    path('translate/', views.translate, name = 'translate'),
]
