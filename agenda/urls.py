from django.urls import path
from .views import *
from . import views

app_name = 'agenda'

urlpatterns = [
    path('agenda/agendar', views.Agendar.as_view(),name='agendar'),
    path('agenda/sucesso', views.Concluiu.as_view(), name='sucesso'),
    path('agenda/list', views.AgendaList.as_view(), name='lista'),
    path('agenda/<slug:slug>', views.AgendaDet.as_view(), name='detalhe'),
]
