from django.contrib import admin
from content.models import *
from content.fields import AdminImageWidget
from django.db import models



class MenuAdmin(admin.ModelAdmin):
    
    list_display = ['name']
    list_editable = ['name']



class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'menu', 'slug', 'published', 'ordering']
    list_editable = ['slug', 'published', 'ordering']

    
class MetaAdmin(admin.ModelAdmin):
    list_display = ['meta_description', 'meta_keywords', 'meta_title', 'meta_author', 'pic_slug', 'published']
    list_editable = ['meta_description', 'meta_keywords', 'meta_title', 'meta_author', 'published']


class TopAdmin(admin.ModelAdmin):
    list_display = ['pic_slug', 'text_small', 'text_big', 'published']
    list_editable = ['text_small', 'text_big', 'published']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }


class  CategoryAdmin(admin.ModelAdmin):
      list_display = ['name']        


class SlideAdmin(admin.ModelAdmin):
    list_display = ['name', 'pic_slug', 'category', 'published', 'published_main', 'ordering']
    list_editable = ['published','ordering', 'published_main']
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget},
    }

   
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Slide, SlideAdmin)  
admin.site.register(Category, CategoryAdmin)

admin.site.register(Snipet)
admin.site.register(Top, TopAdmin)


