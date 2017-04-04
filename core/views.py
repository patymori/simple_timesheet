import time
from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    time_now = time.strftime('%H:%M')
    return render(request, 'home.html', {
        'start_time': time_now,
    })
