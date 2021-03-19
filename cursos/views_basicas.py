from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """API DE CURSOS"""

    serializer_class = CursoSerializer

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = self.serializer_class(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """API das avaliações dos cursos"""

    serializer_class = AvaliacaoSerializer

    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = self.serializer_class(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
