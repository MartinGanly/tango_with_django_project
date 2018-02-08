from django.shortcuts import render

from django.http import HttpResponse

def index(request):
        return HttpResponse("Return to Index <a href='/index'>index</a>")
