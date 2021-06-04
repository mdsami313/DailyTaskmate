from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import CustomRegistrationForm
    
from django.contrib import messages

def register(request):
    if request.method=="POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user Account Created.Login To Get Started!"))
            return redirect('register')
    else:
        register_form = CustomRegistrationForm()
    return render(request, 'register.html', {'register_form':register_form})