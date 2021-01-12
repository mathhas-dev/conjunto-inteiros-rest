from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from .models import Inteiro
from .serializers import InteiroSerializer
from .business import InteiroService
from .validator import valida_inteiro_post


class InteiroViewSet(viewsets.ViewSet):
    """
    Camada View (endpoints) do conjunto dos inteiros
    """

    def list(self, request):
        queryset = Inteiro.objects.all().order_by('pk')
        serializer = InteiroSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Inteiro.objects.all().order_by('pk')
        obj = get_object_or_404(queryset, pk=pk)
        serializer = InteiroSerializer(obj)
        return Response(serializer.data)

    def create(self, request):
        data = valida_inteiro_post.validate(self, request.data)

        Inteiro.objects.create(**data)

        return Response(request.data, status=status.HTTP_201_CREATED)
