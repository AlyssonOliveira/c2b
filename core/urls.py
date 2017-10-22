from django.conf.urls import url
from core import views

urlpatterns = (
    url(r'^customer_add', views.customer_add, name='customer_add'),
    url(r'^anunciar/', views.anunciar, name='anunciar'),
    url(r'^sucesso/$', views.home, name='sucesso'),

    url(r'^likebuyevent/$', views.LikeBuyEvent, name='likebuyevent'),
    url(r'^meusanuncios/$', views.meusanuncios, name='meusanuncios'),
    url(r'^meusanuncios/(?P<slug>[\w-]+)/edit/$',views.meusanuncios, name='meusanuncios_edit'),

)
