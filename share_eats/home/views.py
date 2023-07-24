from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def home_page(request):
    posts = Posts.objects.all().order_by('timestamp')
    return render(request, 'home/cool.html', {'objects':posts})
def about(request):
    return HttpResponse("About This Website")
# Create your views here.
