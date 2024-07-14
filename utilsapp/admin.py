from django.contrib.gis import admin

from utilsapp.models import (ns, wp, pl, rd, row, mh)

# Register your models here.

@admin.register(ns)
class nsAdmin(admin.GISModelAdmin):
    list_display = ("type", "client_gov", "layer", "elevation", 
                    "docupdate")
    

@admin.register(wp)
class wpAdmin(admin.GISModelAdmin):
    list_display = ("type", "client_gov", "layer", "elevation", 
                    "docupdate")

@admin.register(pl)
class plAdmin(admin.GISModelAdmin):
    list_display = ("type", "client_gov", "layer", "elevation", 
                    "docupdate")

@admin.register(rd)
class rdAdmin(admin.GISModelAdmin):
    list_display = ("type", "client_gov", "layer", "elevation", 
                    "docupdate")

@admin.register(row)
class rowAdmin(admin.GISModelAdmin):
    list_display = ("type", "client_gov", "layer", "elevation", 
                    "docupdate")

@admin.register(mh)
class mhAdmin(admin.GISModelAdmin):
    list_display = ("layer", "handle", "elevation", 
                    "docupdate")
