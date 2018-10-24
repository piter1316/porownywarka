from urllib import request

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import generic

from porownanie_cen.models import Produkt


def wszystkie_ceny_view(request):
    products_list = Produkt.objects.all()
    query = request.GET.get('q')
    paginator = Paginator(products_list, 15)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
    }
    if query:
        products = products_list.filter(kodtowaru__contains=query).order_by('cenakoncowa_eur')

    return render(request, 'wszystkie_ceny/produkty.html', context)



# class ProductView(generic.ListView):
#     template_name = 'wszystkie_ceny/produkty.html'
#     context_object_name = 'all_products'
#
#
#     def get_queryset(self,request):
#         query = request.GET.get('q')
#         return Produkt.objects.all()
