from django.conf.urls import url
import product.views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    # url(r'^article/get/(?P<category_id>\d+)/(?P<article_id>\d+)/$', article.views.article),

    url(r'^(?P<category_id>\d+)/$', product.views.products),
    url(r'^supports/$', product.views.supports),
    url(r'^product/(?P<category_id>\d+)/(?P<product_id>\d+)/$', product.views.product),
    url(r'^support/(?P<support_id>\d+)/$', product.views.support),


    # url(r'^videos/page/$', article.views.articles),

    # url(r'^videos/only/$', article.views.video_only),

    # url(r'^writtens/only/$', article.views.written_only),

    # url(r'^article/page/(?P<category_id>\d+)/(?P<art_page_number>\d+)/(?P<left_right>\d+)/$', article.views.article_left_right),

    url(r'^hardware/$', product.views.hardware),
    url(r'^software/$', product.views.software),

    # url(r'^category/get/(?P<category_id>\d+)/$', article.views.category),

    # url(r'^author/get/(?P<author_id>\d+)/$', article.views.authors),

    # url(r'^tag/get/(?P<tag_id>\d+)/$', article.views.tags),

    # url(r'^article/addcomment/(?P<article_id>\d+)/$', article.views.addcomment),
    #  url(r'^page/article/addlike/(?P<article_id>\d+)/$', article.views.addlike),
    #  url(r'^writtens/page/$', article.views.articles),
    # url(r'^writtens/page/(\d+)/$', article.views.articles),
    # #url(r'^videos/page/(\d+)/$', article.views.articles),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

# urlpatterns = [
#     url(r'^videos/get/(?P<category_id>\d+)/(?P<article_id>\d+)/$', article.views.article),
#     url(r'^$', 'article.views.callactions', name='callactions'),
#     # url(r'^page/article/addlike/(?P<article_id>\d+)/$', article.views.addlike),
#     # url(r'^article/addcomment/(?P<article_id>\d+)/$', article.views.addcomment),
#     url(r'^page/$', article.views.articles),
#     url(r'^catalog/$', article.views.catalog),
#     # url(r'^videos/page/(\d+)/$', article.views.articles),
#     url(r'^article/page/(?P<art_page_number>\d+)/(?P<left_right>\d+)/$', article.views.article_left_right),
#     url(r'^writtens/page/$', article.views.articles),
#     # url(r'^writtens/page/(\d+)/$', article.views.articles),
#     # url(r'^$', article.views.articles),
#     url(r'^category/get/(?P<category_id>\d+)/$', article.views.category),
#     url(r'^author/get/(?P<author_id>\d+)/$', article.views.authors),
#     url(r'^tag/get/(?P<tag_id>\d+)/$', article.views.tags),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += staticfiles_urlpatterns() + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )