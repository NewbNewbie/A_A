from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('differ_total', views.toal_differ, name='differ_total')
]
