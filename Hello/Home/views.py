from django.shortcuts import render , HttpResponse
from datetime import datetime
from Home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable" : " this is sent "
    }
    return render(request , 'index.html', context)

def about(request):
    return render(request , 'about.html' )

def services(request):
    return render(request , 'services.html')

def contact(request): 
    if request.method == "POST":
        email = request.POST.get('email')
        passw =request.POST.get('passw')
        addr = request.POST.get('addr')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        contact = Contact(email=email,passw=passw,addr=addr,city=city,state=state,zip=zip,date = datetime.today())
        contact.save()
    return render(request , 'contact.html')

