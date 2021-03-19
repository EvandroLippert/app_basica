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

        Tem uma nested relationship para, ao realizar o get do Curso,
        retornar também uma lista das avaliações existentes

        Atenção ao utilizá-lo, pois quanto mais dados exibidos, maior o tamanho do arquivo e, por conseguinte,
        pior a performance da API
    """
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    """
    Outra forma de exibir os campos relacionados entre os modelos é utilizar a classe HyperlinkedRelatedField
    
    Essa classe exibirá links para as avaliações
    """

    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
