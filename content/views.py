# # -*- coding: utf-8 -*-
# from django.db import models
# from django.http import HttpResponse
# from django.template import Context, loader
# from django.views.decorators.cache import cache_page
# from django.core.cache import cache
# from django.shortcuts import redirect, render, get_object_or_404
# from content.models import *

# from slideshow.models import *
# from django.core.mail import send_mail, EmailMessage
# from turn.models import EmailTurn, SmsTurn
# from suds.client import Client



# def clear_cache(request):
#     cache.clear()
#     return redirect('/')



# def home(request):
    
    

#     return render(request, 'index.html', )
    



# def callback(request):
#     if 'name' in request.POST:
#         name = unicode(request.POST['name'])
#     else:
#         name = '__'
#     tel = str(request.POST['tel'])
    
#     e = EmailTurn(name=u'Заказ ювелирки', to='yrki@inbox.ru', title=u"Заказ ювелирки %s" % tel, text=u'Контактное лицо: %s \nТелефон: %s' %(name, tel))
#     e.save()
#     e = EmailTurn(name=u'Заказ ювелирки', to='zolotiryki@gmail.com', title=u"Заказ ювелирки %s" % tel, text=u'Контактное лицо: %s \nТелефон: %s' %(name, tel))
#     e.save()

#     s = SmsTurn(name=name,to='+380934996314', text=u'Контактное лицо: %s \nТелефон: %s' %(name, tel))
#     s.save()

    
#     import threading
#     t = threading.Thread(target=send_messages)
#     t.start()
#     return HttpResponse("ok")



# def send_messages():
#     e = EmailTurn.objects.filter(published=0)
#     s = SmsTurn.objects.filter(published=0)
    
#     for i in e:
#         try:
#             msg = EmailMessage(i.title, i.text, u"jcdeesign@gmail.com", [u"webmagic@mail.ua", i.to])
#             msg.content_subtype = "html"
#             msg.send()
#             i.published = 1
#             i.save()
#         except:
#             pass
    
#     for i in s:
#         try:
#             client = Client('http://turbosms.in.ua/api/wsdl.html')
#             r = client.service.Auth(login='osvita',password='1qaz2wsx')
#             r = client.service.SendSMS(sender='SheekComUa',destination='+'+i.to, text=i.text)
#             i.published = 1
#             i.save()
#         except:
#             pass
    
