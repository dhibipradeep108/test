from django.http import HttpResponse

def home(request) :
    return HttpResponse("<h3> Home page </h3>")