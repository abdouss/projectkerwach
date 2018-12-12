from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
User = settings.AUTH_USER_MODEL

from django.urls import reverse



class Categorie(models.Model):
	Name   =models.CharField(max_length=300,unique=True,verbose_name='Categorie')
	slug = models.SlugField(unique=True)

	def __unicode__(self):
	    return self.Name

	class Meta:
	    ordering = ['-id']

class Souscategorie(models.Model):
	Name   =models.CharField(max_length=300,unique=True,verbose_name='Sous_Categorie')
	slug   =models.SlugField(unique=True)

	def __unicode__(self):
	    return self.Name


class Produit(models.Model):


	Reference          =models.CharField(max_length=300,blank=True,null=True)
	Marque             =models.CharField(max_length=300,blank=True,null=True)
	Collection         =models.CharField(max_length=200,blank=True,null=True)
	description        =models.TextField(blank=True,null=True)
	Genre              =models.CharField(max_length=300,blank=True,null=True)
	PVPM               =models.CharField(max_length=300,blank=True,null=True)
	slug               =models.SlugField(unique=True)

	user               =models.ForeignKey(User,on_delete=models.CASCADE)
	categorie          =models.ForeignKey(Categorie,on_delete=models.CASCADE)
	souscategorie      =models.ForeignKey(Souscategorie,on_delete=models.CASCADE)


	def __unicode__(self):
		return self.Marque

	def _get_unique_slug(self):
	    slug = slugify(self.Marque)
	    unique_slug = slug
	    num = 1
	    while Produit.objects.filter(slug=unique_slug).exists():
	        unique_slug = '{}-{}'.format(slug, num)
	        num += 1
	    return unique_slug

	def save(self, *args, **kwargs):
	    if not self.slug:
	        self.slug = self._get_unique_slug()
	    super(Produit, self).save()


