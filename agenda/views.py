from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.urls import path
from django.shortcuts import render
from agenda.models import Agendamento
from django.contrib.auth.decorators import login_required

#@login_required
class Agendar(CreateView):
    model = Agendamento
    fields = ['nivel','dF','dM','professor',
    'nome','sobrenome', 'matricula', 'turno','email','cell','slug',
    ]
    template_name = 'agenda/form.html'
    success_url = reverse_lazy('sucesso')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento de Aula'
        context['botaoA'] = 'Agenda!'
        return context

class Concluiu(TemplateView):
    template_name = 'agenda/sucesso.html'
#class Sucesso(CreateView):
#    template_name = 'agenda/sucess.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento Concluido'
        context['texto'] = 'Seu agendamento foi concluido com sucesso, escolha uma das opções abaixo ou selecione no menu.'
        context['botaoA'] = 'Novo Agendamento'
        context['botaoB'] = 'Perfil'
        context['botaoC'] = 'Lista de Agendamentos'
        return context

#Listagem e Detalhamento
#@login_required
class AgendaList(ListView):
    model = Agendamento
    def get_querysert(self):
        self.agendamento_list = Agendamento.objects.filter(usuario=self.request.user)
        return self.agendamento_list
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento Concluido'
        context['texto'] = 'Seu agendamento foi concluido com sucesso, escolha uma das opções abaixo ou selecione no menu.'
        context['botaoA'] = 'Novo Agendamento'
        context['botaoB'] = 'Perfil'
        context['botaoC'] = 'Inicio'
        return context
#@login_required
class AgendaDet(DetailView):
    model = Agendamento
