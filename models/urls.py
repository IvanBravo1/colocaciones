from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^usuario/nuevo$', views.nuevo_usuario),
        url(r'^usuario/nuevo/empresa$', views.nuevo_usuario_empresa),
        url(r'^usuario/nuevo/desocupado$', views.nuevo_usuario_desocupado),
        url(r'^$', views.ingresar),
        url(r'^privado/$', views.privado),
        url(r'^cerrar/$', views.cerrar),
        url(r'^inicio/$', views.inicio),
        url(r'^eleccion/$', views.eleccion),
        url(r'^nueva/$', views.crear_oferta),
        url(r'^oferta/(?P<pk>[0-9]+)/edit/$', views._oferta, name='editar_oferta'),
        url(r'^oferta/(?P<pk>[0-9]+)/delete/$', views.eliminar_oferta, name="eliminar_oferta"),
        url(r'^oferta/(?P<pk>[0-9]+)/$', views.oferta_completa, name="oferta_completa"),
        url(r'^oferta/usuario/(?P<pk>[0-9]+)/$', views.oferta_usuario, name="oferta_usuario"),

]
