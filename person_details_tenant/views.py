from django.shortcuts import render
from .models import Person2

def tenant_views(request):
    tenant = Person2.objects.all()
    return render(request,'basic.html',{'tenant':tenant})
