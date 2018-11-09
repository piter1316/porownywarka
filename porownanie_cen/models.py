from django.db import models
from django.urls import reverse


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    nazwa = models.CharField(db_column='nazwa', max_length=200)
    logo = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('porownanie_cen:detail', kwargs={'pk': self.pk})

    class Meta:
        managed = True
        db_table = 'Brandy'


class Produkt(models.Model):
    klucz = models.CharField(db_column='klucz', max_length=128)
    kodtowaru = models.CharField(db_column='kodTowaru', primary_key=True, max_length=128)
    kontrahentkod = models.CharField(db_column='kontrahentKod', max_length=64)
    kontrahentcennik = models.CharField(db_column='kontrahentCennik', max_length=16)
    opis = models.CharField(max_length=255, blank=True, null=True)
    gruparabatowa_1 = models.CharField(db_column='grupaRabatowa_1', max_length=64, blank=True, null=True)
    gruparabatowa_2 = models.CharField(db_column='grupaRabatowa_2', max_length=64, blank=True, null=True)
    gruparabatowa_3 = models.CharField(db_column='grupaRabatowa_3', max_length=64, blank=True, null=True)
    cenakatalogowa = models.DecimalField(db_column='cenaKatalogowa', max_digits=12, decimal_places=4, blank=True,
                                         null=True)
    walutakatalogowa = models.CharField(db_column='walutaKatalogowa', max_length=3, blank=True, null=True)
    cenakoncowa = models.DecimalField(db_column='cenaKoncowa', max_digits=12, decimal_places=4, blank=True, null=True)
    walutakoncowa = models.CharField(db_column='walutaKoncowa', max_length=3, blank=True, null=True)
    cenakatalogowa_eur = models.DecimalField(db_column='cenaKatalogowa_EUR', max_digits=12, decimal_places=4,
                                             blank=True, null=True)
    cenakoncowa_eur = models.DecimalField(db_column='cenaKoncowa_EUR', max_digits=12, decimal_places=4, blank=True,
                                          null=True)
    moq = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    dataimportu = models.DateField(db_column='dataImportu', null=True, blank=True, auto_now_add=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.kodtowaru

    class Meta:
        managed = True
        db_table = 'Produkty'
        unique_together = (('kodtowaru', 'kontrahentkod', 'kontrahentcennik'),)
