
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


def index_view(request):
     return render(request,"website/index.html")


def about_view(request):
    return render(request,"website/about.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
            messages.success(request, "Done")
            return redirect('website:contact')
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {'form': form})