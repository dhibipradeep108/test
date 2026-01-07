from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Contact
from django.views.generic import ListView
from django.http import HttpResponse, FileResponse
from reportlab.pdfgen import canvas
import csv, io

class ContactListView(ListView) :
    paginate_by = 2
    model = Contact
    
def listing(request) :
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "contacts.html", {"page" : page_obj})

def all_contacts(request) :
    response = HttpResponse(
        content_type = "text/csv",
        headers =  {"Content-Disposition" : 'attachement; filename = "data.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["Name", "Phone Number"])
    contacts = Contact.objects.all()
    for contact in contacts :
        writer.writerow([contact.name, contact.phno])
    return response

def gen_pdf(request) :
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello World")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment = True, filename = "hello.pdf")

def simpleblocktag(request) :
    return render(request, 'test.html', context = {"site" : "contacts"})