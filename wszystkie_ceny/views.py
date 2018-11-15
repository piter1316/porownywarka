import re
from _mysql import result

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from porownanie_cen.models import Produkt


@login_required()
def wszystkie_ceny_view(request):
    products_list = Produkt.objects.select_related('brand')[:20]

    query = request.GET.get('q')
    result = None
    not_found_tip = None
    by_code = None
    info = False
    kod_query = None
    in_wszystkie_produkty = True

    if query:
        kod_query = query.replace("'", '')
        for char in query:
            if char in re.sub(r'[a-zA-Z0-9]', '', char):
                query = query.replace(char, "")
        result = Produkt.objects.filter(kodtowaru=kod_query).select_related('brand')
        if result:
            result = list(result)

        if not result:
            info = True
            result = Produkt.objects.filter(klucz=query).select_related('brand')

        if not result:
            info = False
            not_found_tip = Produkt.objects.filter(klucz__istartswith=query)[:10]

    context = {
        'result': result,
        'products': products_list,
        'query': query,
        'not_found_tip': not_found_tip,
        'by_code': by_code,
        'info': info,
        'kod_query': kod_query,
        'in_wszystkie_produkty': in_wszystkie_produkty,
    }
    return render(request, 'wszystkie_ceny/produkty.html', context)
