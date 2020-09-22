from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from app1.models import Site
from app1.models import SitePosts

# Create your views here.
def index(request):
	
	return render(request,'index.html',)
	
def details_views(request,id):
	sitePosts = get_object_or_404(Site, id=id)
	photos = SitePosts.objects.filter(post=sitePosts)
	return render(request, 'details.html', {
		"sitePosts": sitePosts,
		"photos":photos
	})

def contact(request):
	return render(request,'contact.html')

def services(request):
	return render(request,'services.html')

def work(request):
	dbData = {"data": Site.objects.all(),
	"completed": Site.objects.all().filter(status="Completed"),
	"ongoing": Site.objects.all().filter(status="Not completed")}
	return render(request,'work.html',dbData)