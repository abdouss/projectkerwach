from django.contrib import admin

# Register your models here.
from .models import Categorie,Produit,Souscategorie

admin.site.register(Categorie)
admin.site.register(Souscategorie)
admin.site.register(Produit)