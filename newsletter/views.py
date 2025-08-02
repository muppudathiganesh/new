# newsletter/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberManualForm, SubscriberModelForm
from .models import Subscriber

def signup_manual(request):
    if request.method == "POST":
        form = SubscriberManualForm(request.POST)
        if form.is_valid():
            Subscriber.objects.create(**form.cleaned_data)
            messages.success(request, "Thank you for subscribing!")
            return redirect('signup_manual')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SubscriberManualForm()
    return render(request, 'signup_manual.html', {'form': form})

def signup_modelform(request):
    if request.method == "POST":
        form = SubscriberModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            return redirect('signup_modelform')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SubscriberModelForm()
    return render(request, 'signup_modelform.html', {'form': form})
