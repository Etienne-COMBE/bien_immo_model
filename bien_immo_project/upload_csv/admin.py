from django.contrib import admin
from .models import Bien

# Register your models here.

@admin.register(Bien)
class RequestBien(admin.ModelAdmin):
    list_display = [field.name for field in Bien._meta.get_fields()]
    search_fields = ["departement"]