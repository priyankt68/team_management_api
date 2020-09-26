from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("index url")



class Members(View):
    def get(self, request):
        
    
        return HttpResponse('result')