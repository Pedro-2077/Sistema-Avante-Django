from django.contrib import admin
from django.urls import path,include
from .views import *


#TODO cadastro_externo/ cadastro_atividade/ inscricao/ .exist()
urlpatterns = [

    path('cadastro_externo/', cadastro_externo, name='cdE'),
    path('cadastro_atividade/', cadastro_atividade, name='cdA'),
    path('cadastro_atividade_servico/', cadastro_servico, name='cdS'),
    path('inscricao_aula/', inscricao_aula, name='inscricao_aula'),
    path('api/horarios/<int:atividade_id>/', get_horarios, name='get_horarios'),
    path('api/responsaveis/<int:atividade_id>/<str:horario>/',get_responsaveis, name='get_responsaveis'),

    path('inscricao_servico/', inscricao_servico, name='inscricao_servico'),
    path('api/horarios_servico/<int:servico_id>/', get_horarios_servico, name='get_horarios_servico'),
    path('api/responsaveis_servico/<int:servico_id>/<str:horario>/', get_responsaveis_servico, name='get_responsaveis_servico'),
    path('api/dia_atividade/<int:servico_id>/', get_dia_atividade, name='get_dia_atividade'),

    #path('inscricao/', inscricao, name='insc'),


    path('update_aula/<int:id>/', update_aula, name='update_aula'),
    path('update_servico/<int:id>/', update_servico, name='update_servico'),
    path('update_usuario_externo/<int:id>/', update_usuario_externo, name='update_usuario_externo'),
    path('update_usuario_interno/<int:id>/', update_usuario_interno, name='update_usuario_interno'),


    #feito
    path('lista_aula/', lista_aula, name='lista_aula'),
    path('vizualizar_aula/<int:id>', vizualizar_aula, name='vizualizar_aula'),
    path('lista_servico/', lista_servico, name='lista_servico'),
    path('vizualizar_servico/<int:id>', vizualizar_servico, name='vizualizar_servico'),

    path('lista_usuario_externo/', lista_usuario_externo, name='lista_usuario_externo'),
    path('vizualizar_usuario_externo/<int:id>', visualizar_usuario_externo, name='vizualizar_usuario_externo'),

    path('visualizar_usuario_interno/<int:id>', visualizar_usuario_interno, name='visualizar_usuario_interno'),

    path('lista_usuario_interna/', lista_usuario_interno, name='lista_usuario_interno'),

    path('deletar_aula/<int:id>/', deletar_aula, name='deletar_aula'),
    path('deletar_servico/<int:id>/', deletar_servico, name='deletar_servico'),
    path('deletar_usuario_interno/<int:id>/', deletar_usuario_interno, name='deletar_usuario_interno'),
    path('deletar_usuario_externo/<int:id>/', deletar_usuario_externo, name='deletar_usuario_externo'),
]

