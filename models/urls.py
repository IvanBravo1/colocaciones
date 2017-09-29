from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^usuario/nuevo$', views.nuevo_usuario),
        url(r'^usuario/nuevo/empresa$', views.nuevo_usuario_empresa),
        url(r'^usuario/nuevo/desocupado$', views.nuevo_usuario_desocupado),
        url(r'^ingresar/$', views.ingresar),
        url(r'^privado/$', views.privado),
        url(r'^cerrar/$', views.cerrar),
        url(r'^inicio/$', views.inicio),
        url(r'^eleccion/$', views.eleccion),
    ]
