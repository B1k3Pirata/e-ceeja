from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import *

#---CADASTRO DE DADOS DO ALUNO
class EstudoC(CreateView):
    model = EstudoM
    fields = ['cad','nivel']
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('alunoc')

class UsuarioC(CreateView):
    model = Aluno
    fields = ['nome','snome']
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('pessoais')

class PessoalCreate(CreateView):
    model = Pessoal
    fields = ["nasc", "sexo",
        "raca", "qprenm", "prenm", "filia_1", "filia_2",
        "nacio", "qnacio", "ufnasc"]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('documentos')

class DocCreate(CreateView):
    model = Doc
    fields = [
        "qpcer", "tpcerl", "nocer", "licer", "flcer", "emtcr", "cartc", "ufcrt",
        "cidcrt", "qrg", "norg", "orgrg", "ufrg", "dtrg", "cpf", "pasp",
    ]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('endereço')

class EndCreate(CreateView):
    model = End
    fields = [
        "end", "num", "muni", "cep",
        "comp","brr", "uncon", "qzon",
        "ct1", "ct2"
    ]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('saude')

class SaudeCreate(CreateView):
    model = Sau
    fields = [
        "aep","cego","bv","sc","sd","da","di","dm",
        "df","ai","srt","sasp","tdi","ahs"
    ]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('dados-sociais')

class SocialCreate(CreateView):
    model = Soc
    fields = [
        "bcp", "pbf", "pbt", "peti"
    ]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('locomocao-aluno')

class TranspCreate(CreateView):
    model = Transp
    fields = [
        "pprte","pbfa","qserv","urb","rod","aqua","trm",
    ]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('procedencia-aluno')

class ProcedenciaCreate(CreateView):
    model = Proc
    fields = [
        "nesc","pore1a","pore2a","pore3a",
        "pore4a","comec","anx","idtnv","fase",
        "turno","modal","seq","rat",
    ]
    template_name = 'usrs/form.html'
    success_url = reverse_lazy('inscrever')

from django.contrib.auth.models import User
from .forms import *

class AssinaCreate(CreateView):
    form_class = Registro
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('conclui-cadastro')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de Usuario'
        context['botao']  = 'Cadastrar'
        context['icone']  = '<i class="fa fa-check" aria-hidden= "true"></i>'
        return context

class Concluiu(TemplateView):
    template_name = 'usrs/sucess.html'
#-----
