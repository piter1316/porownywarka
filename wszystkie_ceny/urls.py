from django.conf.urls import url
from . import views

app_name = 'wszystkie_ceny'

urlpatterns = [
    url(r'^produkty/$', views.wszystkie_ceny_view, name='produkty'),
]