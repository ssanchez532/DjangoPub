from django import forms
from .models import Datos_Usuario

class DatosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['numero_documento'].widget.attrs['onkeypress'] = 'return soloNumeros(event)'
        self.fields['celular'].widget.attrs['onkeypress'] = 'return soloNumeros(event)'
        self.fields['ingresos'].widget.attrs['onkeypress'] = 'return soloNumeros(event)'
        self.fields['primer_nombre'].widget.attrs['onkeypress'] = 'return soloLetras(event)'
        self.fields['segundo_nombre'].widget.attrs['onkeypress'] = 'return soloLetras(event)'
        self.fields['primer_apellido'].widget.attrs['onkeypress'] = 'return soloLetras(event)'
        self.fields['segundo_apellido'].widget.attrs['onkeypress'] = 'return soloLetras(event)'
        self.fields['actividad'].widget.attrs['onkeypress'] = 'return soloLetras(event)'
    class Meta:
        model = Datos_Usuario
        fields = '__all__'
        widgets = {
            'numero_documento': forms.TextInput(attrs={'class': 'style-form-django'}),
            'celular': forms.TextInput(attrs={'class': 'style-form-django'}),
            'ciudad': forms.TextInput(attrs={'class': 'style-form-django'}),
            'direccion': forms.TextInput(attrs={'class': 'style-form-django'}),
            'ingresos': forms.TextInput(attrs={'class': 'style-form-django'}),
            'actividad': forms.TextInput(attrs={'class': 'style-form-django'}),
        }
