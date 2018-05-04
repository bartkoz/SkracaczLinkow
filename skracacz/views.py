from django.shortcuts import render, redirect
from .models import Link
from .forms import LinkShortener
from django.http import HttpResponsePermanentRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LinkShortener(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            form.save()
            return render(request, 'skracacz/skrocone.html', {})
    else:
        form = LinkShortener()
    return render(request, 'skracacz/index.html', {})

def skrocone(request):
    return render(request, 'skracacz/skrocone.html', {})
