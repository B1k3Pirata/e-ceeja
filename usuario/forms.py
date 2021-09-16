from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class NivelF(forms.Form):
    class Meta:
        model = EstudoM
        fields = ['cad']

class AlunoF(forms.Form):
    class Meta:
        model = Aluno
        fields = '__all__'

class PessoalF(forms.Form):
    class Meta:
        model = Pessoal
        fields = '__all__'

class DocF(forms.Form):
    class Meta:
        model = Doc
        fields = '__all__'

class EndF(forms.Form):
    class Meta:
        model = End
        fields = '__all__'

class SauF(forms.Form):
    class Meta:
        model = Sau
        fields = '__all__'

class SocF(forms.Form):
    class Meta:
        model = Soc
        fields = '__all__'

class TranspF(forms.Form):
    class Meta:
        model = Transp
        fields = '__all__'

class ProcF(forms.Form):
    class Meta:
        model = Proc
        fields = '__all__'

class Registro(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = [
            'username','email', 'password1', 'password2'
        ]
