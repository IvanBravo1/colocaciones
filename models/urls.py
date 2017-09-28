from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^usuario/nuevo$', views.nuevo_usuario),
        url(r'^ingresar/$', views.ingresar),
        url(r'^privado/$', views.privado),
        url(r'^cerrar/$', views.cerrar),
        url(r'^inicio/$', views.inicio),
    ]
