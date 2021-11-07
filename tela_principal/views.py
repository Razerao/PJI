from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Avisos, Atas, Outros, Comentarios
import json




def home(request):
    if request.session.get('usuario'):
        avisos = Avisos.objects.all()
        atas = Atas.objects.all()
        outros = Outros.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'avisos': avisos, 'atas': atas, 'outros': outros, 'request_usuario': request_usuario, 'usuario_id': request.session.get('usuario')})
    else:
        return redirect('/auth/login/?status=2')

def aviso(request, id):
    if request.session.get('usuario'):
        aviso = Avisos.objects.get(id = id)
        return render(request, 'aviso.html', {'aviso': aviso})
    else:
        return redirect('/auth/login/?status=2')

def ata(request, id):
    if request.session.get('usuario'):
        ata = Atas.objects.get(id = id)
        return render(request, 'ata.html', {'ata': ata})
    else:
        return redirect('/auth/login/?status=2')

def outro(request, id):
    if request.session.get('usuario'):
        outro = Outros.objects.get(id = id)
        return render(request, 'outro.html', {'outro': outro})
    else:
        return redirect('/auth/login/?status=2')
    
def comentarios(request):
    usuario_id = int(request.POST.get('usuario_id'))
    comentario = request.POST.get('comentario')
    

    comentario_instancia = Comentarios(usuario_id = usuario_id,
                                       comentario = comentario)
    comentario_instancia.save()

    comentarios = Comentarios.objects.filter().order_by('-data')
    somente_nomes = [i.usuario.nome for i in comentarios]
    somente_comentarios = [i.comentario for i in comentarios]
    comentarios = list(zip(somente_nomes, somente_comentarios))

    return HttpResponse(json.dumps({'status': '1', 'comentarios': comentarios }))

def avisos(request):
    if request.session.get('usuario'):
        avisos = Avisos.objects.all()
        return render(request, 'avisos.html', {'avisos': avisos})
    else:
        return redirect('/auth/login/?status=2')

def atas(request):
    if request.session.get('usuario'):
        atas = Atas.objects.all()
        return render(request, 'atas.html', {'atas': atas})
    else:
        return redirect('/auth/login/?status=2')

def outros(request):
    if request.session.get('usuario'):
        outros = Outros.objects.all()
        return render(request, 'outros.html', {'outros': outros})
    else:
        return redirect('/auth/login/?status=2')
