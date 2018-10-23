from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms as F
from porownanie_cen import forms
from porownanie_cen.forms import UpdateBrand
from .models import Brand
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'porownanie_cen/index.html'
    context_object_name = 'all_brands'

    def get_queryset(self):
        return Brand.objects.all()


class DetailView(generic.DetailView):
    model = Brand
    template_name = 'porownanie_cen/produkty.html'





class BrandUpdate(UpdateView):
    model = Brand
    form_class = UpdateBrand
    success_url = reverse_lazy('porownanie_cen:index')






class BrandDelete(DeleteView):
    model = Brand
    success_url = reverse_lazy('porownanie_cen:index')
    # usuwanie bez potwierdzającego template
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)



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
