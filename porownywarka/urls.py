from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from porownanie_cen.views import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^porownanie_cen/', include('porownanie_cen.urls')),
    url(r'^wszystkie_ceny/', include('wszystkie_ceny.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', login_required(IndexView.as_view()), name="home"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
