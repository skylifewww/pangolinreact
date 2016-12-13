from django import template
# from django.contrib.admin.util import lookup_field
# from django.core.exceptions import ObjectDoesNotExist
# from django.core.urlresolvers import NoReverseMatch, reverse
# from django.db.models import ForeignKey
# from django.template.defaulttags import NowNode
# from django.utils.safestring import mark_safe
from django.shortcuts import render_to_response, redirect, get_object_or_404
from content.models import *
from product.models import Category, Support


register = template.Library()




@register.inclusion_tag('meta/title.html')
def meta_title():
    
    meta = get_object_or_404(Meta, published=1)
    return {'title': meta.meta_title}


@register.inclusion_tag('meta/author.html')
def meta_author():
    
    meta = get_object_or_404(Meta, published=1)
    return {'author': meta.meta_author}


@register.inclusion_tag('meta/description.html')
def meta_description():
    
    meta = get_object_or_404(Meta, published=1)
    return {'description': meta.meta_description}


@register.inclusion_tag('meta/keywords.html')
def meta_keywords():
    
    meta = get_object_or_404(Meta, published=1)
    return {'keywords': meta.meta_keywords}


@register.inclusion_tag('top/image_back.html')
def top_image_back():
    
    top = get_object_or_404(Top, published=1)
    # return {'image_back': top.image_back}
    return {'image_back': top.slug}


@register.inclusion_tag('top/text_small.html')
def top_text_small():
    
    top = get_object_or_404(Top, published=1)
    return {'text_small': top.text_small}


@register.inclusion_tag('top/text_big.html')
def top_text_big():
    
    top = get_object_or_404(Top, published=1)
    return {'text_big': top.text_big}

@register.inclusion_tag('footer/category_footer.html')
def category_footer():
    
    categories = Category.objects.filter(published=1).order_by('ordering')
    return {'categories': categories} 


@register.inclusion_tag('footer/support_footer.html')
def support_footer():
    
    supports = Support.objects.filter(published=1).order_by('ordering')
    return {'supports': supports}     


# @register.inclusion_tag('slides/slides.html')
# def slides():
    
#     slides = Slide.objects.filter(published=1).order_by('ordering')
#     return {'slides': slides}


# @register.inclusion_tag('menu/main_menu.html')
# def main_menu():
    
#     menu = Menu.objects.get(pk=1)
#     items = MenuItem.objects.filter(menu=menu, published=1).order_by('ordering')
#     return {'items': items}














# @register.inclusion_tag('comments/comments.html')
# def comments(paket, item_model, item_id):
#     from comments.models import Comments
#     nodes = Comments.objects.filter(paket=paket, item_model=item_model,item_id=item_id, published=1)
#     return {'nodes':nodes, 'paket':paket, 'item_model':item_model, 'item_id':item_id}


# @register.filter(name='suit_conf')
# def suit_conf(name):
#     value = get_config(name)
#     return mark_safe(value) if isinstance(value, str) else value


# @register.tag
# def suit_date(parser, token):
#     return NowNode(get_config('HEADER_DATE_FORMAT'))


# @register.tag
# def suit_time(parser, token):
#     return NowNode(get_config('HEADER_TIME_FORMAT'))


# @register.filter
# def field_contents_foreign_linked(admin_field):
#     """Return the .contents attribute of the admin_field, and if it
#     is a foreign key, wrap it in a link to the admin page for that
#     object.

#     Use by replacing '{{ field.contents }}' in an admin template (e.g.
#     fieldset.html) with '{{ field|field_contents_foreign_linked }}'.
#     """
#     fieldname = admin_field.field['field']
#     displayed = admin_field.contents()
#     obj = admin_field.form.instance

#     if not hasattr(admin_field.model_admin,
#                    'linked_readonly_fields') or fieldname not in admin_field \
#         .model_admin \
#         .linked_readonly_fields:
#         return displayed

#     try:
#         fieldtype, attr, value = lookup_field(fieldname, obj,
#                                               admin_field.model_admin)
#     except ObjectDoesNotExist:
#         fieldtype = None

#     if isinstance(fieldtype, ForeignKey):
#         try:
#             url = admin_url(value)
#         except NoReverseMatch:
#             url = None
#         if url:
#             displayed = "<a href='%s'>%s</a>" % (url, displayed)
#     return mark_safe(displayed)


# @register.filter
# def admin_url(obj):
#     info = (obj._meta.app_label, obj._meta.module_name)
#     return reverse("admin:%s_%s_change" % info, args=[obj.pk])


# @register.simple_tag
# def suit_bc(*args):
#     return utils.value_by_version(args)


# @register.assignment_tag
# def suit_bc_value(*args):
#     return utils.value_by_version(args)

