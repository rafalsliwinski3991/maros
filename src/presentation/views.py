from django.shortcuts import render
from django.utils import timezone
from .models import Postmod
from .models import Refmod
from .models import Tabormod
# Create your views here.
def home(request):
	title = 'Główna'
	return render(request, "mainpage.html", {'title': title})

def dokonania(request):
	posts = Postmod.objects.order_by('-published_date')
	title = 'Dokonania'
	#posts = PostUp.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'dokonania.html', {'posts': posts,'title': title})

def kontakt(request):
	title = 'Kontakt'
	return render(request, "kontakt.html", {'title': title})

def oferta(request):
	title = 'Oferta'
	return render(request, "oferta.html", {'title': title})

def ofirmie(request):
	title = 'O firmie'
	return render(request, "ofirmie.html", {'title': title})

def referencje(request):
	title = 'Referencje'
	refs = Refmod.objects.all()
	return render(request, "referencje.html", {'refs' : refs, 'title' : title})

def tabor(request):
	title = 'Tabor'
	tabors = Tabormod.objects.all()
	return render(request, "tabor.html", {'tabors' : tabors, 'title' : title})
