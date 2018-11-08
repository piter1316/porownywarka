from django.shortcuts import render
from porownanie_cen.models import Produkt


def wszystkie_ceny_view(request):
    products_list = Produkt.objects.raw("select * from produkty limit 20")
    query = request.GET.get('q')
    result = None
    not_found_tip = None
    by_code = None
    info = False
    in_wszystkie_produkty = 1
    kod_query = None

    if query:
        kod_query = query.replace("'",'')
        query = query.replace('-', '')
        query = query.replace('/', '')
        query = query.replace('_', '')
        query = query.replace(' ', '')
        query = query.replace('"', "")
        not_found_tip = Produkt.objects.raw("SELECT * FROM produkty WHERE kodtowaru LIKE %s LIMIT 10", (kod_query + "%",))

        result = Produkt.objects.raw("SELECT * from produkty where kodtowaru = '{}' order by cenakoncowa_eur".format(kod_query))
        info = False
        if not result:
            info = True
            result = Produkt.objects.raw(
                "SELECT * from produkty where klucz = '{}' order by cenakoncowa_eur".format(query))

        #     by_key = True
        #     result = Produkt.objects.raw("SELECT * from produkty where klucz = '{}' order by cenakoncowa_eur".format(query))

    context = {
        'result': result,
        'products': products_list,
        'query': query,
        'not_found_tip': not_found_tip,
        'by_code': by_code,
        'info': info,
        'in_wszystkie_produkty': in_wszystkie_produkty,
        'kod_query': kod_query,
    }
    return render(request, 'wszystkie_ceny/produkty.html', context)
