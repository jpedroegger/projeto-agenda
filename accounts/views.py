from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)  # Autenticação com django.

    if not user:  # Em caso de usuário inválido, mensagem de erro será levantada.
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Você fez login com sucesso.')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)  # Logout com Django.
    messages.success(request, 'Deslogado com sucesso.')
    return redirect('index')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')
    # Todos os campos precisam estar preenchidos.
    if not nome or not sobrenome or not email or not usuario or not senha2 or not senha:
        messages.error(request, 'Preencha todos os campos para cadastrar.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)  # Valida o e-mail.
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'A senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'O usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem.')
        return render(request, 'accounts/cadastro.html')

    # Checa se o usuário já existe na base de dados.
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já cadastrado.')
        return render(request, 'accounts/cadastro.html')

    # Checa se o email já existe na base de dados.
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado.')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Cadastro efetuado com sucesso!\n Faça o login abaixo.')

    user = User.objects.create_user(
        username=usuario,
        email=email,
        password=senha,
        first_name=nome,
        last_name=sobrenome,
    )
    user.save()  # Cria o usuário e salva na base de dados.

    return redirect('login')


@login_required(redirect_field_name='login')  # Área disponíveis apenas para logados.
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContato(request.POST, request.FILES)

    if not form.is_valid():  # Validar formulário com Django.
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    descricao = request.POST.get('descricao')  # Pega a descrição inserida pelo usuário e salva na variável.

    if len(descricao) < 10:
        messages.error(request, 'Faça uma descrição mais detalhada.')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()  # Cria o formulário.
    messages.success(request, f'Contato {request.POST.get("nome")} salvo com sucesso.')
    return redirect('dashboard')
