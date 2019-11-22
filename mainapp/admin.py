from django.contrib import admin

# Register your models here.

from mainapp.models import China_Item
from mainapp.models import Korea_Item
admin.site.register(China_Item)
admin.site.register(Korea_Item)
