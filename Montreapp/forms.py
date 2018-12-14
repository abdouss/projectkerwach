from .models import Produit,PointVente
from django import forms

import datetime
from .models import User

class ProduitForm(forms.ModelForm):

	class Meta:
		model =Produit
		fields ='__all__'




class PointVentForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        	model = PointVente
        	fields = ("first_name",
                  "last_name",  
                  "email",
                  "admin",
                  'username',)


