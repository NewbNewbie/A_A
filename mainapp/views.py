from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'mainapp/index.html', {
    })


def toal_differ(request):
	return render(request, 'mainapp/total_differ.html', {

	})
