from django.shortcuts import render, redirect

common_timezones = {
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "New York": "America/New_York",
}

def translate(request) :
    context = {"text" : "नमस्ते"}
    return render(request, 'translate.html', context)

def set_timezone(request) :
    if request.method == 'POST' :
        request.session["django_timezone"] = request.POST["tz"]
        return redirect('home')
    else :
        return render(request, 'timezone.html', {"tz" : common_timezones})