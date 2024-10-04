from django.urls import path
from . import views

urlpatterns = [
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('', views.listar_eventos, name='listar_eventos'),
    path('eventos/registrar/<int:evento_id>/', views.registrar_usuario, name='registrar_usuario'),
    path('eventos/actualizar/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('eventos/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('eventos/actualizar_registro/<int:registro_id>/', views.actualizar_registro_evento, name='actualizar_registro_evento'),
    path('eventos/usuarios/<int:evento_id>/', views.listar_usuarios, name='listar_usuarios'),

]
