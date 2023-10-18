from django.contrib import admin
from .models import Classes, Professors, ClassCodes

# Register your models here.
admin.site.register([Classes, Professors, ClassCodes])
