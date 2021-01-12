from django.db import transaction, models as db
from .models import Inteiro


class InteiroService():
    def list(self):
        return Inteiro.objects.all().order_by('pk')

    @transaction.atomic
    def create(self, data):
        print(data)
        # try:
        #     qtd = int(data['nItens'])
        #     if qtd >= 1 and qtd <= 1000:
        #         lista = []

        #         for n in range(qtd):
        #             try:
        #                 k = int(data['lista'])
        #             except Exception as e:
        #                 print("ERRO: " + str(e))
        #             if k >= -1000 and k <= 1000 and k not in lista:
        #                 lista.append(k)

        #         listaOrdenada = sorted(lista)
        #         for n in listaOrdenada:
        #             print(n)

        # except Exception as e:
        #     print("Insira Apenas números entre: 1 e 1000!")

    def single(self):
        return self.list

    def get(self, pk=None):
        if pk is None:
            raise Exception("Não foi possível recuperar o objeto.")
        return self.single().get(pk=pk)
