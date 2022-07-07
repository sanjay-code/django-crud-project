from django import forms
from .models import People_data

class InputData(forms.ModelForm):
	class Meta:
		model = People_data
		fields = ['name','email','phone']
		labels = {
			'name':'Enter Name',
			'email':'Enter Email',
			'phone':'Enter Roll',

		}

		widgets = {

			'name':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'phone':forms.NumberInput(attrs={'class':'form-control'}),

		}	
