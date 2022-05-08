from django.shortcuts import render, get_object_or_404, Http404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from accounts.models import FormContato
from django.contrib.auth.decorators import login_required, permission_required


def index(request):

    contatos = Contato.objects.order_by('-id').filter(mostrar=True)

    # Método de paginação proposto pela documentação Django.
    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos,
    })


def ver_contato(request, contato_id):
    # Levanta Erro 404 se contato não for localizado.
    contato = get_object_or_404(Contato, id=contato_id)  
    # Impede que o contato seja exibido, se não estiver com mostrar ativado.
    if not contato.mostrar:  
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })


def busca(request):
    # Armazeno o termo buscado na variável.
    termo = request.GET.get('termo')  
    # Indica que se o termo de busca estiver vazio ou None.
    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Preencha um termo de pesquisa.'
        )
        return redirect('index')

    # Concat concatena as chaves da base de dados que serão buscadas.
    campos = Concat('nome', Value(' '), 'sobrenome', Value(' '), 'telefone')

    # Q permite usar | como OR. Neste caso, ou nome completo ou telefone.
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


@login_required
@permission_required('contatos.change_contato', raise_exception=True)  # Checa permissão do usuário.
def editar_contato(request, contato_id):

    contato = get_object_or_404(Contato, id=contato_id)
    form = FormContato(instance=contato)

    context = {'form': form,
               'contato': contato}

    if request.method == 'POST':

        form = FormContato(request.POST, request.FILES, instance=contato)

        descricao = request.POST.get('descricao')

        if len(descricao) < 5:
            messages.error(request, 'Faça uma descrição mais detalhada.')
            return render(request, 'contatos/editar_contato.html', context)

        if form.is_valid():
            form.save()
            messages.success(request, 'Contato editado com sucesso.')
            return render(request, 'contatos/ver_contato.html', {'contato': contato})

    return render(request, 'contatos/editar_contato.html', context)


@permission_required('contatos.delete_contato', raise_exception=True)
def deletar_contato(request, contato_id):

    contato = get_object_or_404(Contato, id=contato_id)
    contato.delete()  # Deleta o contato usuando Django.
    excluido = messages.success(request, 'Contato excluído com sucesso.')
    return redirect('/', excluido)

