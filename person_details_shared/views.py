from django.shortcuts import render
from .models import Person

def shared_view(request):
    shared = Person.objects.all()
    return render(request,'index.html',{'shared':shared})