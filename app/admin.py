from django.contrib import admin

from app.models import Car

# Register your models here.
class CarFilter(admin.ModelAdmin):
    list_display = ("brand", "model", "year")
    list_display_links = ('brand', 'model', 'year')
    list_filter = ('brand', 'year')
    search_fields = ('brand', 'model', 'year')

admin.site.register(Car, CarFilter)