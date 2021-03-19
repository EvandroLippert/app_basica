from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins

from cursos.models import Curso, Avaliacao
from cursos.serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import IsSuperUser


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
                          )
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['GET'])
    def avaliacoes(self, request, pk=None):
        """
        Buscar todas as avaliações do curso determinado

        E retorna um resultado por página
        """
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


"""
Quando sua classe herda as funções da viewsets, 
a sua API fornece todos os verbos HTTP (GET, POST, PUT, PATCH DELETE).

Entretanto, se você deseja que sua API ofereça apenas determinadas ações,
é possível customizá-la selecionando apenas os verbos que deseja que ela execute.


Por exemplo, na função abaixo, retirei a opção de GET ALL, ou seja, de listar todos os objetos
"""


class AvaliacaoViewSet(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
