from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dash_home(request):
    if request.method == 'GET':
        return render(request, 'oficial-home.html')


@login_required(login_url='login')
def opcoes_cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/opcoesCadastros.html')


def erro_page(request, exception):
    return render(request, 'erro.html')