from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'map.html')

def notice(request):
    return render(request, 'notice.html')

def timetable(request):
    return render(request,'timetable.html')

def detail(request):
    return render(request,'detail.html')

