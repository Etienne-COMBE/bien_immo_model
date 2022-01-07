from django.contrib import admin
from .models import Bien

# Register your models here.
class BienAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bien, BienAdmin)