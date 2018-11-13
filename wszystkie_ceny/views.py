from _mysql import result

from django.shortcuts import render
from porownanie_cen.models import Produkt

def wszystkie_ceny_view(request):
    products_list = Produkt.objects.raw("""SELECT 
        produkty.*,
        brandy.nazwa
        from produkty 
        left join  brandy  on produkty.brand_id = brandy.id
        limit 20""")

    query = request.GET.get('q')
    result = None
    not_found_tip = None
    by_code = None
    info = False
    kod_query = None
    in_wszystkie_produkty = True

    if query:
        kod_query = query.replace("'", '')
        query = query.replace('-', '')
        query = query.replace('/', '')
        query = query.replace('_', '')
        query = query.replace(' ', '')
        query = query.replace('"', "")
        query = query.replace('\t', "")
        not_found_tip = Produkt.objects.raw("SELECT * FROM produkty WHERE kodtowaru LIKE %s LIMIT 10",
                                            (kod_query + "%",))
        result = Produkt.objects.raw("""SELECT 
        produkty.*,
        brandy.nazwa
        from produkty 
        left join  brandy  on produkty.brand_id = brandy.id
        where kodtowaru = '{}' order by cenakoncowa_eur""".format(kod_query))
        # if result:
        #     result = list(result)
        #     result.append("BY_KOD_TOWARU")
        if not result:
            info = True
            result = Produkt.objects.raw(
                """SELECT produkty.*,
                brandy.nazwa
                from produkty 
                left join  brandy  on produkty.brand_id = brandy.id
                where klucz = '{}' order by cenakoncowa_eur""".format(query))
            if not result:
                info = False

                not_found_tip = Produkt.objects.raw("SELECT produkty.*, brandy.nazwa FROM produkty "
                                                "left join  brandy  on produkty.brand_id = brandy.id"
                                                " WHERE klucz LIKE %s LIMIT 10",
                                                (query + "%",))

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
