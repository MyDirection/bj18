from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    return HttpResponse("hello world")

def list_page(request):
    return redirect('/index')


 





