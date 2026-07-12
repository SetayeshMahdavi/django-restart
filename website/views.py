
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index_view(request):
     return render(request,"website/index.html")


def about_view(request):
    return render(request,"website/about.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد.')
            return redirect('website:contact')
    else:
        form = ContactForm()

    return render(request, "website/contact.html", {'form': form})