from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import Contact
from .models import Headquarters
# Create your views here.

def ContactView(request):
    Headquarter = Headquarters.objects.all()[:3]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        context = {"messages":True}
        return HttpResponseRedirect(request.path_info,context)
        
    return render(request, 'contact.html')
