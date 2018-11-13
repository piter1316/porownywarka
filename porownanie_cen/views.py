from django.db.models import Min
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms as F
from porownanie_cen import forms
from porownanie_cen.forms import UpdateBrand
from .models import Brand, Produkt
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'porownanie_cen/index.html'
    context_object_name = 'all_brands'

    def get_queryset(self):
        return Brand.objects.all()


class BrandUpdate(UpdateView):
    model = Brand
    form_class = UpdateBrand
    # fields = ['nazwa', 'logo']
    success_url = reverse_lazy('porownanie_cen:index')


class BrandDelete(DeleteView):
    model = Brand
    success_url = reverse_lazy('porownanie_cen:index')

    # usuwanie bez potwierdzającego template
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required()
def brand_create(request):
    if request.method == 'POST':
        form = forms.CreateBrand(request.POST, request.FILES)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()

            return redirect('porownanie_cen:index')
    else:

        form = forms.CreateBrand()
    return render(request, 'porownanie_cen/brand_add.html', {'form': form})


def brand_details(request, pk):
    query = request.GET.get('q')
    codes_to_query = None
    by_price = []
    all_products = Produkt.objects.raw(
        "select * from produkty where brand_id ={} and kodtowaru ='{}' ".format(pk, query))
    base_view = Produkt.objects.raw("select * from produkty where brand_id ={} limit 10".format(pk))
    brand = Brand.objects.raw("select id,nazwa from brandy where id={}".format(pk))
    final_result = []
    code_price = []
    brand_id = pk
    kontrahenci = Produkt.objects.values('kontrahentkod').distinct().filter(brand_id=pk)
    kontrahenci_length = len(kontrahenci)

    if query:
        codes_to_query = query.splitlines()
        for code in codes_to_query:
            kod_query = code.replace("'", '')
            code = code.replace('-', '')
            code = code.replace('/', '')
            code = code.replace('_', '')
            code = code.replace(' ', '')
            code = code.replace('"', "")
            code = code.replace('\t', "")

            if code != '':
                result = Produkt.objects.values('klucz', 'kodtowaru').filter(kodtowaru=kod_query, brand_id=pk).annotate(
                    Min('cenakoncowa_eur'))

                if not result:
                    result = Produkt.objects.values('klucz', 'kodtowaru').filter(klucz=code, brand_id=pk).annotate(
                        Min('cenakoncowa_eur'))
                    if not result:
                        code_price.append(code)
                if result:

                    code_price.append(result)

            for kontrahent in kontrahenci:
                price = Produkt.objects.values('kodtowaru', 'cenakoncowa_eur', 'kontrahentkod').filter(
                        kontrahentkod=kontrahent['kontrahentkod'], kodtowaru=kod_query, brand_id=pk)
                if not price:
                    price = Produkt.objects.values('klucz', 'cenakoncowa_eur', 'kontrahentkod').filter(
                        kontrahentkod=kontrahent['kontrahentkod'], klucz=code, brand_id=pk)
                by_price.append(price)

    for result in by_price:
        final_result.append(result.values('kontrahentkod', 'cenakoncowa_eur', 'klucz').order_by('cenakoncowa_eur'))

    context = {
        'products': all_products,
        'base_view': base_view,
        'brand': brand,
        'kontrahenci': kontrahenci,
        'query': query,
        'codes_to_query': codes_to_query,
        'by_price': by_price,
        'final_result': final_result,
        'kontrahenci_length': kontrahenci_length,
        'code_price': code_price,
        'brand_id': brand_id,
    }
    return render(request, 'porownanie_cen/produkty.html', context)
