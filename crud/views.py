from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Usuario, RegistroEvento

def crear_evento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')
        ubicacion = request.POST.get('ubicacion')
        Evento.objects.create(titulo=titulo, descripcion=descripcion, fecha=fecha, ubicacion=ubicacion)
        return redirect('listar_eventos')
    return render(request, 'eventos/crear_evento.html')

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

def registrar_usuario(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        usuario, created = Usuario.objects.get_or_create(email=email, defaults={'nombre': nombre})
        RegistroEvento.objects.create(evento=evento, usuario=usuario)
        return redirect('listar_eventos')
    return render(request, 'eventos/registrar_usuario.html', {'evento': evento})

def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descripcion = request.POST.get('descripcion')
        evento.fecha = request.POST.get('fecha')
        evento.ubicacion = request.POST.get('ubicacion')
        evento.save()
        return redirect('listar_eventos')
    return render(request, 'eventos/actualizar_evento.html', {'evento': evento})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})

def actualizar_registro_evento(request, registro_id):
    registro = get_object_or_404(RegistroEvento, id=registro_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        if nombre and email:
            usuario, created = Usuario.objects.get_or_create(email=email, defaults={'nombre': nombre})
            registro.usuario = usuario
            registro.save()
            return redirect('listar_eventos')
    return render(request, 'eventos/actualizar_registro_evento.html', {'registro': registro})

def listar_usuarios(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    usuarios = Usuario.objects.filter(registroevento__evento=evento)
    return render(request, 'eventos/listar_usuarios.html', {'evento': evento, 'usuarios': usuarios})
