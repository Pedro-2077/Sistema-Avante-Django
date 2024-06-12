from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import Inscrever_AulaForm, AtividadeForm, Usuario_ExternoForm, ServicoAtividadeForm, Inscrever_ServicoForm
from rolepermissions.decorators import has_permission_decorator
from django.contrib.auth.decorators import login_required
from .models import Inscrever_Aula, Atividade, Usuario_Externo, Servico, DiaAtividade
from perfis.models import Users
from perfis.forms import UserFormTemplate
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError



# TODO Fazer Update e Delete dos usuarios Internos e Externo
@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def cadastro_externo(request):
    if request.method == 'GET':
        form = Usuario_ExternoForm()
        return render(request, 'cadastro_UserExterno.html', {'form': form})

    if request.method == 'POST':
        form = Usuario_ExternoForm(request.POST)

        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            usuario = Usuario_Externo.objects.filter(cpf=cpf)

            if usuario.exists():
                messages.add_message(request, messages.ERROR, 'Usuario ja existe!')
                return render(request, 'cadastro_UserExterno.html', {'form': form})

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuario Externo cadastrado com sucesso!')
            return redirect(reverse('cdE'))

        else:
            print(form.errors)
            messages.add_message(request, messages.ERROR,
                                 'Erro ao cadastrar usuario externo. Verifique os dados e tente novamente.')
            return render(request, 'cadastro_UserExterno.html', {'form': form})



@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def update_usuario_externo(request, id):
    usuario = get_object_or_404(Usuario_Externo, id=id)
    if request.method == 'POST':
        form = Usuario_ExternoForm(request.POST, instance=usuario)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuário Externo atualizado com sucesso!')
            return redirect(reverse('update_usuario_externo', args=[id]))
    else:
        form = Usuario_ExternoForm(instance=usuario)
    return render(request, 'update/update_usuario_externo.html', {'form': form})



@xframe_options_exempt
@login_required(login_url='login')
def update_usuario_interno(request, id):
    usuario = get_object_or_404(Users, pk=id)
    if request.method == 'POST':
        form = UserFormTemplate(request.POST, instance=usuario)
        print(form.errors)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usuário Interno atualizado com sucesso!')
            return redirect(reverse('update_usuario_interno', args=[id]))  
    else:
        form = UserFormTemplate(instance=usuario)
    return render(request, 'update/update_usuario_interno.html', {'form': form, 'usuario': usuario})


@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_atividade')
def cadastro_atividade(request):
    if request.method == 'GET':
        form = AtividadeForm()
        return render(request, 'cadastro_atividade_aula/cadastro_atividade_aula.html', {'form': form})

    elif request.method == 'POST':
        form = AtividadeForm(request.POST)

        if form.is_valid():
            atividade = form.save(commit=False)
            form.save_m2m()
            atividade.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade cadastrada com sucesso!')
            return redirect(reverse('cdA'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'cadastro_atividade_aula/cadastro_atividade_aula.html', {'form': form})


def inscricao_aula(request):
    if request.method == 'GET':
        form = Inscrever_AulaForm()
        formu = Inscrever_ServicoForm()
        return render(request, 'inscricao_aula_e_servico/inscricao_aula_e_servico.html', {'form': form, 'formu': formu})
    elif request.method == 'POST':
        form = Inscrever_AulaForm(request.POST)
        formu = Inscrever_ServicoForm()
        if form.is_valid():
            print(request.POST)
            aluno = form.cleaned_data['nome_aluno']
            ativida_nome = form.cleaned_data['nome_atividade']
            horario = form.cleaned_data['horario_aula']
            responsavel = form.cleaned_data['responsavel']

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Inscrição cadastrada com sucesso!')
            return redirect(reverse('inscricao_aula'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'inscricao_aula_e_servico/inscricao_aula_e_servico.html', {'form': form,'formu': formu })


def get_horarios(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    horario = atividade.hora_atividade  # Diretamente o campo de hora
    horarios_data = [{'hora': horario.strftime('%H:%M')}]
    return JsonResponse({'horarios': horarios_data})


def get_responsaveis(request, atividade_id, horario):
    # Filtra a atividade com base no ID e no horário
    atividade = get_object_or_404(Atividade, id=atividade_id, hora_atividade=horario)

    # Obtém o responsável pela atividade
    responsavel = atividade.responsavel

    # Cria a resposta JSON com as informações do responsável
    data = {
        'id': responsavel.id,
        'username': responsavel.username,
        'email': responsavel.email,
        'first_name': responsavel.first_name,
        'last_name': responsavel.last_name,
    }

    return JsonResponse(data)


def inscricao_servico(request):
    if request.method == 'GET':
        formu = Inscrever_ServicoForm()
        form = Inscrever_AulaForm()
        return render(request, 'inscricao_aula_e_servico/inscricao_aula_e_servico.html.html', {'formu': formu, 'form':form})
    elif request.method == 'POST':
        formu = Inscrever_ServicoForm(request.POST)
        form = Inscrever_AulaForm(request.POST)


        print('aqui')
        if formu.is_valid():
            aluno = formu.cleaned_data['aluno']
            servico_atividade = formu.cleaned_data['servico_atividade']
            hora_servico = formu.cleaned_data['hora_servico']
            dia_servico = formu.cleaned_data['dia_servico']
            responsavel = formu.cleaned_data['responsavel']

            formu.save()
            messages.success(request, 'Inscrição cadastrada com sucesso!')
            return redirect('inscricao_aula')
        else:
            print(formu.errors)
            messages.error(request, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'inscricao_aula_e_servico/inscricao_aula_e_servico.html', {'formu': formu, 'form':form})


def get_horarios_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    horarios = [servico.hora_inicio.strftime('%H:%M')]
    return JsonResponse({'horarios': horarios})


def get_responsaveis_servico(request, servico_id, horario):
    # Filtra o serviço com base no ID
    servico = get_object_or_404(Servico, id=servico_id)

    # Obtém o responsável do serviço
    responsavel = servico.responsavel

    # Cria a resposta JSON com as informações do responsável
    data = {
        'id': responsavel.id,
        'username': responsavel.username,
        'email': responsavel.email,
        'first_name': responsavel.first_name,
        'last_name': responsavel.last_name,
    }

    return JsonResponse(data)


def get_dia_atividade(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    dia_atividade = servico.dia_atividade.strftime('%Y-%m-%d')
    return JsonResponse({'dia_atividade': dia_atividade})


@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_atividade')
def cadastro_servico(request):
    if request.method == 'GET':
        form = ServicoAtividadeForm()
        return render(request, 'cadastro_atividade_servicos/cadastro_atividade_servicos.html', {'form': form})

    elif request.method == 'POST':
        form = ServicoAtividadeForm(request.POST)
        if form.is_valid():

            dia_atividade = form.cleaned_data['dia_atividade']
            responsavel = form.cleaned_data['responsavel']
            if Servico.objects.filter(dia_atividade=dia_atividade, responsavel=responsavel).exists():
                messages.add_message(request, messages.ERROR, 'Já existe um serviço cadastrado para esse responsável nesse dia')
                return render(request, 'cadastro_atividade_servicos/cadastro_atividade_servicos.html', {'form': form})

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade cadastrada com sucesso!')
            return redirect(reverse('cdS'))
        else:
            messages.add_message(request, messages.ERROR, 'Ocorreu algum erro ao cadastrar')
            return render(request, 'cadastro_atividade_servicos/cadastro_atividade_servicos.html', {'form': form})


# UPDATE---------------------------------------------------------------
@xframe_options_exempt
@login_required(login_url='login')
@has_permission_decorator('cadastro_externo')
def update_aula(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        print(form)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Atividade atualizada com sucesso!')
            return redirect(reverse('update_aula', args=[id]))
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'update/update_aula.html', {'form': form, 'atividade': atividade})


@xframe_options_exempt
@login_required(login_url='login')
def update_servico(request,id):
    servico = get_object_or_404(Servico, pk=id)
    if request.method == 'POST':
        form = ServicoAtividadeForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            return redirect(reverse(update_servico, args=[id]))
    else:
        form = ServicoAtividadeForm(instance=servico)

    return render(request, 'update/update_servico.html', {'form': form, 'servico': servico})
# ---------------------------------------------------------------------



# Vizualizar---------------------------------------------------------------
@xframe_options_exempt
@login_required(login_url='login')
def vizualizar_aula(request, id):
    vizualizar = get_object_or_404(Atividade, id=id)
    return render(request, 'vizualizar_aula/vizualizar_aula.html', {'vizualizar': vizualizar})


@xframe_options_exempt
@login_required(login_url='login')
def vizualizar_servico(request, id):
    vizualizar = get_object_or_404(Servico, id=id)
    return render(request, 'vizualizar_servico/vizualizar_servico.html', {'vizualizar': vizualizar})

@xframe_options_exempt
@login_required(login_url='login')
def visualizar_usuario_externo(request, id):
    userExterno = get_object_or_404(Usuario_Externo, id=id)
    return render(request, 'visualizar/visualizar_usuario_externo.html', {'userExterno': userExterno})


@xframe_options_exempt
@login_required(login_url='login')
def visualizar_usuario_interno(request, id):
    userInterno= get_object_or_404(Users, id=id)
    return render(request, 'visualizar/visualizar_usuario_interno.html', {'userInterno': userInterno})
# ---------------------------------------------------------------------



# lista---------------------------------------------------------------
@login_required(login_url='login')
def lista_usuario_interno(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        internoList = Users.objects.all()
        internoList = internoList.filter(first_name__icontains=pesquisa)

    else:
        internoList = Users.objects.all()
        return render(request, 'lista/listagemUsuariosInternos.html', {'internoList': internoList})

    return render(request, 'lista/listagemUsuariosInternos.html', {'internoList': internoList})


@login_required(login_url='login')
def lista_usuario_externo(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        externoList = Usuario_Externo.objects.all()
        externoList = externoList.filter(nome__icontains=pesquisa)


    else:
        externoList = Usuario_Externo.objects.all()
        return render(request, 'lista/listagemUsuariosExternos.html', {'externoList': externoList})

    return render(request, 'lista/listagemUsuariosExternos.html', {'externoList': externoList})


@xframe_options_exempt
@login_required(login_url='login')
def lista_aula(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        aulaList = Atividade.objects.all()
        aulaList = aulaList.filter(nome_atividade__icontains=pesquisa)


    else:
        aulaList = Atividade.objects.all()
        return render(request, 'lista/listagemAulas.html', {'aulaList': aulaList})

    return render(request, 'lista/listagemAulas.html', {'aulaList': aulaList})


@xframe_options_exempt
@login_required(login_url='login')
def lista_servico(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:

        servicoList = Servico.objects.all()
        servicoList = servicoList.filter(nome_servico__icontains=pesquisa)

    else:
        servicoList = Servico.objects.all()

    return render(request, 'lista/listagemServicos.html', {'servicoList': servicoList})

# ---------------------------------------------------------------------


# Delete---------------------------------------------------------------

@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
def deletar_cliente(request, slug):
    usuario = get_object_or_404(Usuario_Externo, slug=slug)
    form = Usuario_ExternoForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        messages.add_message(request, messages.SUCCESS, 'Deletado com Sucesso')
        return redirect(reverse('lista'))

    return render(request, 'delete/deletar_externo.html', {'form': form})


@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
@require_POST
def deletar_aula(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    atividade.delete()
    return JsonResponse({'message': 'Aula deletada com sucesso!'})


@login_required(login_url='login')
@has_permission_decorator('cadastro_interno')
@require_POST
def deletar_servico(request, id):
    servico = get_object_or_404(Servico, id=id)
    servico.delete()
    return JsonResponse({'message': 'Serviço deletado com sucesso!'})


def deletar_usuario_interno(request, id):
    usuario = get_object_or_404(Users, id=id)
    usuario.delete()
    return JsonResponse({'message': 'Usuarario Deletado'})

def deletar_usuario_externo(request, id):
    usuario = get_object_or_404(Usuario_Externo, id=id)
    usuario.delete()
    return redirect(reverse('vizualizar_usuario_externo'))
# ---------------------------------------------------------------------

