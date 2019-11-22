from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from mainapp.models import *

def index(request):
    return render(request, 'mainapp/index.html', {
    })


def toal_differ(request):
	queryset = China_Item.objects.raw("SELECT * FROM `mainapp_china_item` WHERE `china_id`")
	for f in queryset:
		print(f)

	return render(request, 'mainapp/total_differ.html', {

	})
