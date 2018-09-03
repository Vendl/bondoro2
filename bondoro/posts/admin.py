from django.contrib import admin
from .models import Programok, Hirek, Tamogatok, Banner

# Register your models here.

admin.site.register(Programok)
admin.site.register(Hirek)
admin.site.register(Tamogatok)
admin.site.register(Banner)
