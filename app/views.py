from django.shortcuts import render


# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from app.forms import *

from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def display(request):
    EUFO=userform()
    EPFO=profileform()
    d={'EUFO':EUFO,'EPFO':EPFO}

    if request.method=="POST" and request.FILES:
        NMUFDO=userform(request.POST)
        NMPFDO=profileform(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('Registration',
            'Regsitartion is Successfulll',
            'phanikumarmeejuru@gmail.com',
            [MUFDO.email],
            fail_silently=False)

            return HttpResponse('REgistration is Successfull')
        else:
            print(NMUFDO.errors)  # Check errors
            print(NMPFDO.errors)  # Check errors
            return HttpResponse('Invalid Data')
    return render(request,'app/display.html',d)
    

class Home(View):
    def get(self,request):
        
        return render(request,'app/home.html')


class SchoolListView(ListView):
    model=School                 # collected all objects of School model
    context_object_name='schools'
    #template_name='app/school_list.html'
    ordering=['name']

class SchoolDetailView(DetailView):
    model=School
    context_object_name='school'
    
class SchoolCreateView(CreateView):
    model=School
    fields='__all__'


class SchoolUpdateView(UpdateView):
    model=School
    fields='__all__'




class SchoolDeleteView(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('list')

















    