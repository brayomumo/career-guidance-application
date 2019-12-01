from django.shortcuts import render
from .models import allcourses

# Create your views here.
def index(request):
    courses = allcourses.objects.all()
    cutoff = 40.028
    cutoff = int(cutoff)
    cutoffD = cutoff + 0.999
    print(cutoffD)
    print(cutoff)
    course = allcourses.objects.filter(cutoffpoints_2018_cp__range=(cutoff,cutoffD))
    for i in course:
        print(i.course_name)
    print("Index")

    return render(request, "base.html", {"courses":courses})

def getcourse(request,cutoff):
    cutoff = int(cutoff)
    cutoffD = cutoff + 0.999
    print(cutoff)  
    course = allcourses.objects.filter(cutoffpoints_2018_cp__range=(cutoff,cutoffD))
    return render(request, "base.html", {"course":course})