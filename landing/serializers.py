from rest_framework import serializers
from landing.models import Aluno


# fields =(__all__) para pegar todos os atributos da model no django-rest
from professor.models import Professor


class AlunoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=255,required=True)
    idade = serializers.IntegerField()
    email = serializers.EmailField()
    prof_favorito = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Professor.objects.all()
    )

    def create(self,validated_data):
        aluno = Aluno.objects.create(**validated_data)
        return aluno
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.email = validated_data.get('email')
        instance.prof_favorito = validated_data.get('prof_favorito')
        instance.save()
        return instance

