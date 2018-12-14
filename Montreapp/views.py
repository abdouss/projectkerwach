from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Produit,PointVente

from .forms import ProduitForm,PointVentForm
from django.views.generic import (DetailView,CreateView,DeleteView,ListView)
from django.urls import reverse

from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                )
import csv,io
from django.urls import reverse_lazy

from django.http import HttpResponse
from django.contrib.auth.models import User


def login_view(request): # users will login with their Email & Password
        title = "Login"
        form = PointVentForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            form.savet()
            # authenticates Email & Password
            return redirect("listproduit")
        context = {"form":form,
        'title':title,
        }

        return render(request, "Montreapp/form.html", context)

class CreateProduit(LoginRequiredMixin,CreateView):

	form_class       =ProduitForm
	model            =Produit
	template_name    ="Montreapp/Forproduit.html"



	def get_success_url(self, *args, **kwargs):
	   return reverse('detailproduit',kwargs={'slug':self.object.slug})



class DetailProduit(DetailView):

	model                =Produit
	template_name        ="Montreapp/detailproduit.html"
	context_object_name  ='produit'




def export_produit(request):
	items        =Produit.objects.all()
	response     =HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="users.csv"'
	writer = csv.writer(response,delimiter =',')
	writer.writerow(['Reference', 'Marque', 'Collection', 'description','Genre','PVPM','slug','categorie','souscategorie'])

	for obj in items:
		 writer.writerow(['obj.Reference', 'obj.Marque', 'obj.Collection', 'obj.description','obj.Genre','obj.PVPM','obj.slug','obj.categorie','obj.souscategorie'])

	return response

class ListProduit(ListView):#lister les nouveaux annonces

	model         =Produit
	template_name ="Montreapp/listproduit.html"
	paginate_by   =15
	context_object_name = 'produits'



class DeleteAnnonce(LoginRequiredMixin,DeleteView):

	model            =Produit
	success_url      =reverse_lazy("listproduit")





class CreatePointVente(LoginRequiredMixin,CreateView):

	form_class       =PointVentForm
	model            =PointVente
	template_name    ="Montreapp/Forpointvente.html"

	def get_success_url(self, *args, **kwargs):
	   return reverse('detailpointvente',kwargs={'slug':self.object.slug})



class DetailPointVente(DetailView):

	model                =PointVente
	template_name        ="Montreapp/detailpointvente.html"
	context_object_name  ='point'

