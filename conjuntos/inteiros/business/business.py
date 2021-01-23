from django.db import transaction, models as db
from inteiros.models import Inteiro
from inteiros.validators import InteiroValidator


class InteiroService():
    def list(self):
        return Inteiro.objects.all().order_by('pk')

    def create(self, data):
        data = InteiroValidator.validate(self, data)

        instance = Inteiro.objects.create(**data)

        return instance

    def single(self):
        return self.list()

    def get(self, pk=None):
        if pk is None:
            raise Exception("Não foi possível recuperar o objeto.")
        return self.single().get(pk=pk)

    def update(self, instance, data, user):
        pass

    def remove(self, instance, user):
        pass
