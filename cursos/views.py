"""


Essa views é a versão otimizada do arquivo views_basicas, ela vem no formato pre-determinado pela classe escolhida

CreateAPIView:

    Tem o método POST


RetrieveAPIView:

    Tem o método GET

ListAPIView:

    Tem o método GET que retorna uma lista

ListCreateAPIView:

    Têm os métodos GET, que retorna uma lista, e o POST

RetrieveUpdateAPIView:

    Têm os métodos GET, PUT e o PATCH


RetrieveDestroyAPIView:

    Têm os métodos GET e o DELETE


RetrieveUpdateDestroyAPIView:

    Têm os métodos GET, DELETE, PUT e PATCH

"""
from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursosAPIView(generics.ListCreateAPIView):
    """Faz o GET de uma lista de itens e o POST de item novo"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Faz o GET, PUT, PACH e DELETE de item"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    """Faz o GET de uma lista de itens e o POST de item novo"""

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        """Sobscrevendo a função original para adicionar filtro com foreing key e por nome"""
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        elif self.kwargs.get('nome'):
            return self.queryset.filter(nome=self.kwargs.get('nome'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Faz o GET, PUT, PACH e DELETE de item"""
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
