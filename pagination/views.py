from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Contact
from django.views.generic import ListView

class ContactListView(ListView) :
    paginate_by = 2
    model = Contact
    
def listing(request) :
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "contacts.html", {"page" : page_obj})