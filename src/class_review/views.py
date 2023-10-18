from django.shortcuts import render, HttpResponse
from .models import Classes


# Create your views here.
def home(request):
    return render(request, "home.html")


def classes(request):
    allClasses = Classes.objects.all()
    return render(request, "classes.html", {"classes": allClasses})
