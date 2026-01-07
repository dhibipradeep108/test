from django.urls import path
from . import views

urlpatterns = [
    path('listing/', views.listing, name = "listing"),
    path('all/', views.all_contacts, name = "all_contacts"),
    path('pdf/', views.gen_pdf, name = "gen_pdf"),
    path('custom_tag/', views.simpleblocktag, name = "custom_tag"),
]