from django import forms
from django.forms import ModelForm
from models import *

class Fregistro(forms.Form):
	usuario=forms.CharField(required=True,help_text="Este campo es requerido")
	farmacia=forms.CharField(required=True,help_text="Este campo es requerido")
	ubicacion=forms.CharField(required=True,help_text="Este campo es obligatorio")
	email=forms.CharField(required=True,help_text="Este campo es requerido")
	password1=forms.CharField(required=True, widget= forms.PasswordInput,help_text="Este campo es obligatorio y mayor a 4 digitos")
	password2=forms.CharField(required=True, widget= forms.PasswordInput,help_text="Este campo es obligatorio y mayor a 4 digitos")
	#verificar si el password tiene mas de 4 digitos
	def clean_password1(self):
		password1 = self.cleaned_data.get('password1','')
		num_words=len(password1)
		if num_words < 4:
			raise forms.ValidationError('ingrese mas de cuatro digitos')
		return password1
	#verificamos si el password es correcto o similar
	def clean_password2(self):
		password1=self.cleaned_data.get('password1','')
		password2=self.cleaned_data.get('password2','')
		if password1 != password2:
			raise forms.ValidationError('Repita el password')
		return password2



