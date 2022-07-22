from rest_framework import serializers
from django.db.models import Avg
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': { 'write_only': True }
        }
        model = Avaliacao
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

    def validate_avaliacao(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError('Avaliação deve ser entre 1 e 5')


class CursoSerializer(serializers.ModelSerializer):
    #Nested Relationship *(Pouco performático)
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #Hyperlinked Related Field *(Menos ruim em termos de performace)
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #Primary key related field *(Mais performatico)
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
    # Pouco performático - Usar signals na model
    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')

        if media is None:
            return 'Ainda sem avaliações'
        return round(media * 2) / 2