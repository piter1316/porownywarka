from django.shortcuts import render
from porownanie_cen.models import Produkt


def wszystkie_ceny_view(request):
    products_list = Produkt.objects.raw("select * from produkty limit 20")
    query = request.GET.get('q')
    result = None
    not_found_tip = None
    by_key = None

    if query:
        query = query.replace('-', '')
        query = query.replace('/', '')
        query = query.replace('_', '')
        query = query.replace(' ', '')
        query = query.replace('"', "")
        not_found_tip = Produkt.objects.raw("SELECT * FROM produkty WHERE kodtowaru LIKE %s LIMIT 10", (query + "%",))
        result = Produkt.objects.raw("SELECT * from produkty where kodtowaru = '{}' order by cenakoncowa_eur".format(query))
        by_key = False
    if not result:
        by_key = True
        result = Produkt.objects.raw("SELECT * from produkty where klucz = '{}' order by cenakoncowa_eur".format(query))

    context = {
        'result': result,
        'products': products_list,
        'query': query,
        'not_found_tip': not_found_tip,
        'by_key': by_key,
    }
    return render(request, 'wszystkie_ceny/produkty.html', context)
