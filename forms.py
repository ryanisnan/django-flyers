from django import forms

from flyers.models import FLYER_TYPE_CHOICES, FORSALE_FLYER_TYPE, LOST_FLYER_TYPE, ForSaleFlyer, LostFlyer, Theme

class FlyerTypeForm(forms.Form):
	flyer_type = forms.ChoiceField(choices=FLYER_TYPE_CHOICES, widget=forms.RadioSelect, initial=FORSALE_FLYER_TYPE)

class ForSaleFlyerForm(forms.ModelForm):
	theme = forms.ModelChoiceField(queryset=Theme.objects.filter(flyer_type=FORSALE_FLYER_TYPE), empty_label=None, widget=forms.RadioSelect)
	class Meta:
		model = ForSaleFlyer
		widgets = {
			'description' : forms.Textarea(attrs={ 'cols' : 100, 'rows' : 5 }),
			'theme' : forms.RadioSelect,
			'currency' : forms.RadioSelect
		}
		
class LostFlyerForm(forms.ModelForm):
	is_reward = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')), widget=forms.RadioSelect, initial=False)
	theme = forms.ModelChoiceField(queryset=Theme.objects.filter(flyer_type=LOST_FLYER_TYPE), empty_label=None, widget=forms.RadioSelect)
	class Meta:
		model = LostFlyer
		widgets = {
			'description' : forms.Textarea(attrs={ 'cols' : 100, 'rows' : 5 }),
			'theme' : forms.RadioSelect
		}