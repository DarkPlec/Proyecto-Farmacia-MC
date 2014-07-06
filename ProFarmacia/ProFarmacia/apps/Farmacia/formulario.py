from django import forms

class loginF(forms.Form):
    usr=forms.CharField(max_length=30)
    pas=forms.CharField(widget=forms.PasswordInput)

class RInventario(forms.Form):
	Name_med=forms.CharField(required=True,help_text="Este campo es obligatorio")
	Cantidad=forms.CharField(required=True,help_text="Este campo es obligatorio")
	Presio=forms.CharField(required=True,help_text="Este campo es obligatorio")
	#Categoria=forms.CharField(max_length=10,choices=Cte,)
	P= 'prescripcion'
	O= 'Oral'
	Sub='Sublingual'
	Pa = 'Parenteral'
	Rc='Rectal'
	T = 'Topica'
	I = 'Inyeccion'
	tr='transdermica'
	In='Inhalada'
	OPTIONS =(
		(P, 'Prescripcion'),#
		(O, 'Oral'),#
		(Sub,'Sublingual'),#
		(Pa, 'Parenteral'),#
		(Rc,'Rectal'),
		(T, 'Topica'),#
		(I, 'Inyeccion'),#
		(tr,'transdermica'),
		(In,'Inhalada'),
            )
	CategoriaM = forms.ChoiceField(widget=forms.Select,choices=OPTIONS)

class BusInvFarm(forms.Form):
	B_med=forms.CharField(required=True,help_text="introdusca el medicamento a buscar")
#class editarM(forms.Form):
#	name_med=forms.CharField()
#	cantidad=forms.CharField()
#	presio=forms.CharField()

class VentaMedicamento(forms.Form):
	N_medicamento=forms.CharField()
	Cant=forms.CharField()
	#presio=forms.CharField()

class EditarU(forms.Form):

	farmacia=forms.CharField(required=True,help_text="Este campo es requerido")
	ubicacion=forms.CharField(required=True,help_text="Este campo es obligatorio")
	email=forms.CharField(required=True,help_text="Este campo es requerido")

class RescatarPassword(forms.Form):
	usuario=forms.CharField(required=True,help_text="Este campo es obligatorio")
	email=forms.CharField(required=True,help_text="Este campo es obligatorio")
