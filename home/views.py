from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello :), you're at the home index.")
    return render(request, "home/index.html")