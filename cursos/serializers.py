"""

Faz a conversão dos objetos python dos models em campos json
e depois esses campos json voltam a ser objetos python

Ou seja, auxilia no registro e na busca de objetos dos models.
"""

from rest_framework import serializers
from django.db.models import Avg

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

    """
    Criar função para validar os dados inseridos
    def validate_nome_do_campo()
    """

    def validate_avaliacao(self, valor):
        if valor in range(0, 6):
            return valor
        raise serializers.ValidationError("A avaliação precisa ser um valor entre 0 e 5")


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

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )

    """
    Para exibir um valor que não é inserido pelo usuário, como a média, por exemplo,
    Devemos instanciar o item, no caso "media_avaliacoes" e criar uma função para formar o valor.
    
    O padrão do nome da função é get_nome_do_campo_criado.
    
    No nosso caso, é get_media_avaliacoes
    
    """

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 0

        return round(media * 2) / 2
