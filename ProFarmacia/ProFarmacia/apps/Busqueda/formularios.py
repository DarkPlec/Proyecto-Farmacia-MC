from django import forms

class B_Global(forms.Form):
	N_Medicamento=forms.CharField(required=True,help_text="Escriba el Medicamento a Buscar")
	#LL=forms.CharField(widget=forms.HiddenInput)
	
class BFarmacia(forms.Form):
	N_Farmacia=forms.CharField(required=True,help_text="Escriba el nombre de la Farmacia")
		