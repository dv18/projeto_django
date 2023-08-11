from django.shortcuts import render
from .models import Usuario

#request é um parametro do django que te peermite acessar os dados da pagina
def home(request):
    return render(request, 'usuarios/home.html')
#render - criar a pagina
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #Exibe todos os usuarios em uma nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request,'usuarios/usuarios.html', usuarios)

