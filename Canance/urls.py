from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarCurso/', views.registrarCurso),
    path('gestion_cursos/eliminarCurso/<codigo>', views.eliminarCurso, name='eliminarCurso'),
    path('gestion_cursos/edicionCurso/<int:codigo>/', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso),
    path('gestion_cursos/', views.home, name='gestion_cursos'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

