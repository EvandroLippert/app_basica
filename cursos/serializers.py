"""

Faz a conversão dos objetos python dos models em campos json
e depois esses campos json voltam a ser objetos python

Ou seja, auxilia no registro e na busca de objetos dos models.
"""

from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    """
        Serializer para o model Avaliação.
    Por questões de privacidade, o campo email é write-only
    """
    class Meta:
        # evitar que o e-mail seja exibido em requisições get
        extra_kwargs = {
            "email": {'write_only': True}
        }
        model = Avaliacao
        # Campos exibidos para o usuário
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    """
        Serializer para o model Curso.
    """
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo'
        )
