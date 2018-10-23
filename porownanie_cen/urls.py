from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
app_name = 'porownanie_cen'

urlpatterns = [
    #/porownanie_cen
    url(r'^$', views.IndexView.as_view(), name='index'),



    #porownanie_cen/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # powownanie_cen/brand/add/
    url(r'brand/add/$', views.brand_create, name='brand-add'),

    # powownanie_cen/brand/23/
    url(r'brand/(?P<pk>[0-9]+)/$', login_required(views.BrandUpdate.as_view()),name='brand-update'),

    # powownanie_cen/brand/23/delete/
    url(r'brand/(?P<pk>[0-9]+)/delete/$', login_required(views.BrandDelete.as_view()), name='brand-delete'),


]

