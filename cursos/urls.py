from django.urls import path

from .views import CursoAPIView, AvaliacaoAPIView, \
    CursosAPIView, AvaliacoesAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='cursos_avaliacoes'),
    path('avaliacoes/<str:nome>/', AvaliacoesAPIView.as_view(), name='avaliacoes_nome'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]
