from django import forms

class Bmedicamento(forms.Form):
	Posicion=forms.CharField(required=True,help_text="Este campo es obligatorio")
	Med_bus=forms.CharField(required=True,help_text="Este campo es obligatorio")
	#LyL=forms.CharField(widget=forms.HiddenInput)

class Bmedicamento2(forms.Form):
	Posicion2=forms.CharField(required=True,help_text="Este campo es obligatorio")
	Med_bus2=forms.CharField(required=True,help_text="Este campo es obligatorio")
	#LyL2=forms.CharField(widget=forms.HiddenInput)

class B_Global(forms.Form):
	N_Medicamento=forms.CharField(required=True,help_text="Escriba el Medicamento a Buscar")
	#LL=forms.CharField(widget=forms.HiddenInput)
