from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import custumregistration
# Create your views here.
def register(request):
    if request.method =='POST':
        register_form = custumregistration(request.POST)
        if register_form.is_valid():
           register_form.save()
           messages.success(request,'account created succesfully')
           return redirect('home')
    else:
        register_form = custumregistration()
    return render(request,'register.html',{'register_form':register_form})