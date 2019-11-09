from django.shortcuts import render
from django.http import HttpResponseNotAllowed

# Create your views here.


def index(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    return render(request, 'index.html')
