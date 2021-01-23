from rest_framework import serializers
from inteiros.models import Inteiro


class InteiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inteiro
        fields = "__all__"
