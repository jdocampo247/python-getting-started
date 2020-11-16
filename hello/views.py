from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.core.cache import cache
import time

from .models import Greeting

TASKS_KEY = "tasks.all"

def index(request):
    tasks = cache.get(TASKS_KEY)
    if not tasks:
        time.sleep(2)  # simulate a slow query.
        tasks = 'Tarea'
        cache.set(TASKS_KEY, tasks)
        print("Usado cache")
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

# Create your views here.
#def index(request):
    #times = int(os.environ.get('TIMES', 3))
    #return HttpResponse('Hello! ' * times)

    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    #return HttpResponse('<pre>' + r.text + '</pre>')

    # return HttpResponse('Hello from Python!')
    #return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
