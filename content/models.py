# -*- coding: utf-8 -*-
from django.db import models

import random
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
import datetime
import mptt
from mptt.fields import TreeForeignKey



def make_upload_path(instance, filename, prefix = False):
    # Переопределение имени загружаемого файла.
    n1 = random.randint(0,10000)
    n2 = random.randint(0,10000)
    n3 = random.randint(0,10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.jpg'
    return u"%s/%s" % (settings.IMAGE_UPLOAD_DIR, filename)



class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name Menu")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = u"Меню"

    
class MenuItem(MPTTModel):
    menu = models.ForeignKey(Menu,null=True, blank=True, verbose_name=u"Меню")
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    # full_text = RichTextField(blank=True, verbose_name="Полное описание")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Родительский пункт меню")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"Пункты меню"
        
    class MPTTMeta:
        order_insertion_by = ['name']
    

    
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name="Category")
    # title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    # metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    # metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    # slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    # parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Родительская категория")
    # published = models.BooleanField(verbose_name="Опубликован")
    # ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)

    def __unicode__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


    
class Meta(models.Model):
    meta_description = RichTextField(blank=True, verbose_name="Мета описание")
    meta_keywords = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    meta_title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    meta_author = models.CharField(max_length=250, blank=True, verbose_name="Автор сайта")
    # favicon = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="favicon.ico")
    favicon_slug = models.CharField(max_length=250, blank=True, verbose_name="Урл favicon")
    published = models.BooleanField(verbose_name="Опубликован", blank=True, default=0)

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name_plural = "Мета описания"
        verbose_name = "Мета описание"

    # def pic(self):
    #     if self.favicon:
    #         return u'<img src="%s" width="70"/>' % self.favicon.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True  

    def pic_slug(self):
        if self.favicon_slug:
            return u'<img src="%s" width="70"/>' % self.favicon_slug
        else:
            return '(none)'
    pic_slug.short_description = 'favicon'
    pic_slug.allow_tags = True       
        

        
class Snipet(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    text = RichTextField(blank=True, verbose_name="Код снипета")
    published = models.BooleanField(verbose_name="Опубликован")
    ordering = models.IntegerField(verbose_name="Порядок сортировки", default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Сниппеты"
        verbose_name = "Сниппет"


class Top(models.Model):
    # image_back = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="Изображение_1200x118")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Урл")
    text_small = models.CharField(max_length=250, blank=True, verbose_name="Обещание")
    text_big = models.CharField(max_length=250, blank=True, verbose_name="Заявка на победу")
    published = models.BooleanField(verbose_name="Опубликован")
    
     
    def __str__(self):
        return self.text_small

    class Meta:
        verbose_name_plural = "Шапки"
        verbose_name = "Шапка"   

    # def pic(self):
    #     if self.image_back:
    #         return u'<img src="%s" width="70"/>' % self.image_back.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True  

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = u'Картинка шапки'
    pic_slug.allow_tags = True   


class Slide(models.Model):
    category = models.ForeignKey(Category, related_name="slides", verbose_name="Category", default="", blank=True, null=True)
    name = models.CharField(max_length=250, verbose_name="Name")
    # image = models.ImageField(upload_to=make_upload_path, blank=True,  verbose_name="Изображение")
    slug = models.CharField(max_length=250, blank=True, verbose_name="Url pic")
    text1 = RichTextUploadingField(blank=True, verbose_name="Text1")
    text2 = RichTextUploadingField(blank=True, verbose_name="Text2")
    published = models.BooleanField(verbose_name="Published", blank=True)
    published_main = models.BooleanField(verbose_name="Published on main", default="", blank=True)
    ordering = models.IntegerField(verbose_name="Ordering", default=0, blank=True, null=True)
    
        
    def __unicode__(self):
        return self.name

    # def pic(self):
    #     if self.image:
    #         return u'<img src="%s" width="70"/>' % self.image.url
    #     else:
    #         return '(none)'
    # pic.short_description = u'Большая картинка'
    # pic.allow_tags = True

    def pic_slug(self):
        if self.slug:
            return u'<img src="%s" width="70"/>' % self.slug
        else:
            return '(none)'
    pic_slug.short_description = 'Slide'
    pic_slug.allow_tags = True   

    class Meta:
        verbose_name_plural = "Slides"
        verbose_name = "Slide"  


  
              
        

        

    
    
