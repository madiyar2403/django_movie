from django.contrib import admin
from .models import Category, Genre, Actor
# Register your models here.
admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)