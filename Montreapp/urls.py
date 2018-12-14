from django.conf.urls import url
from Montreapp import views
from django.urls import re_path
from .views import (login_view)



urlpatterns = [

    re_path(r'^new$',views.CreateProduit.as_view(),name='produitnew'),
    re_path(r'^pointvente/new$',views.CreatePointVente.as_view(),name='pointnew'),

    re_path(r'^detail/(?P<slug>[\w-]+)/$',views.DetailProduit.as_view(),name='detailproduit'),
    re_path(r'^detaile/poinvente/(?P<slug>[\w-]+)/$',views.DetailPointVente.as_view(),name='detailpointvente'),

    re_path(r'^download/csv/$', views.export_produit, name='export_produit'),
    re_path(r'^lister$',views.ListProduit.as_view(),name='listproduit'),
    re_path(r'^produit/(?P<slug>[\w-]+)/remove/$',views.DeleteAnnonce.as_view(),name='delete'),
    re_path(r'^login/$', login_view, name='login'),



]