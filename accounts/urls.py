from django.conf.urls import url

# from accounts.views import LoginView
from .import views



app_name = 'accounts'


urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    # url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]