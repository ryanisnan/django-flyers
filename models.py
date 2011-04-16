#encoding:UTF-8
from django.db.models import Q
from django.db import models


DEFAULT_CURRENCY = 1
CURRENCY_CHOICES = (
	(1, "$"),
	(2, "£")
)

FORSALE_FLYER_TYPE = 1
LOST_FLYER_TYPE = 2

FLYER_TYPE_CHOICES = (
	(FORSALE_FLYER_TYPE, 'For Sale'),
	(LOST_FLYER_TYPE, 'Lost'),
)

"""
Class that represents a theme. A theme
can be associated with a specific Flyer sub-class
"""
class Theme(models.Model):
	name = models.CharField(max_length=32)
	template_filename = models.CharField(max_length=64)
	author = models.CharField(max_length=32)
	website = models.URLField()
	
	flyer_type = models.IntegerField(max_length=32, choices=FLYER_TYPE_CHOICES)
	
	def __unicode__(self):
		return self.name

"""
Base Class that represents a flyer
"""
class Flyer(models.Model):
	date_created = models.DateField(auto_now_add=True)
	
	class Meta:
		abstract = True

"""
Class that represents a for sale flyer
"""
class ForSaleFlyer(Flyer):
	type = FORSALE_FLYER_TYPE
	description = models.TextField(null=True, blank=True)
	currency = models.PositiveSmallIntegerField(choices=CURRENCY_CHOICES, default=DEFAULT_CURRENCY)
	cost = models.DecimalField(max_digits=7, decimal_places=2)
	phone = models.CharField(max_length=16)
	email = models.EmailField(null=True, blank=True)
	image1 = models.ImageField(upload_to='apps/flyers/images')
	
	theme = models.ForeignKey(Theme, limit_choices_to={ 'flyer_type' : FORSALE_FLYER_TYPE })
	
	def __unicode__(self):
		return self.item

"""
Class that represents a lost item flyer
"""
class LostFlyer(Flyer):
	type = LOST_FLYER_TYPE
	item = models.CharField(max_length=48)
	description = models.TextField(null=True, blank=True)
	image1 = models.ImageField(null=True, blank=True, upload_to='apps/flyers/images')
	contact_name = models.CharField(max_length=12)
	contact_phone = models.CharField(max_length=16)
	contact_email = models.EmailField(null=True, blank=True)
	is_reward = models.BooleanField(default=False)
	
	theme = models.ForeignKey(Theme, limit_choices_to={ 'flyer_type' : LOST_FLYER_TYPE })
	
	def __unicode__(self):
		return self.item