from django import forms
from django.utils.html import format_html
from .models import *

class BrandForm(forms.ModelForm):

	

	class Meta:
		model = Brand
		fields = '__all__'

		widgets = {
			'geometry': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex. POINT(12.123 12.123)'})
		
		}

		

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)




class updateBrandForm(forms.ModelForm):

	class Meta:
		model = Brand
		fields = '__all__'
		widgets = {
			'geometry': forms.TextInput(attrs={'class':'form-control','placeholder':'Ex. POINT(12.123 12.123)'}),
			
		}

	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for field in self.fields.values():
			field.label=field.label.title()
			field.widget.attrs['Placeholder'] = ('Enter '+ field.label).title()
			field.widget.attrs['class'] = 'form-control'
			if field.required:
				field.label = format_html('<span style="color:red">* </span> {}', field.label)



# dynamic_form/models.py



# dynamic_form/forms.py

from .models import DynamicFormModel

class DynamicForm(forms.ModelForm):
	class Meta:
		model = DynamicFormModel
		fields = ['name', 'category', 'subcategory']

		widgets = {
			'category': forms.Select(attrs={'class':'form-control'}),
			'subcategory': forms.Select(attrs={'class':'form-control'}),
		}

	category_choice=(
		('Food','Food'),
		('Clothing','Clothing'),
		('Shoes','Shoes'),
		('Electronics','Electronics'),
		('Other','Other'),
	)

	category = forms.ChoiceField(choices=category_choice, widget=forms.Select(attrs={'class':'form-control'}))
	

