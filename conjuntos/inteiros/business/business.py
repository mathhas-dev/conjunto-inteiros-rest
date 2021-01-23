from django.db import transaction, models as db
from inteiros.models import Inteiro
from inteiros.validators import InteiroValidator


class InteiroService():
    def list(self, usuario):
        pass

    def single(self, pk):
        pass

    def get(self, pk):
        pass

    def create(self, data):

        data = InteiroValidator.validate(self, data)

        instance = Inteiro.objects.create(**data)

        return instance

    def update(self, instance, data, user):
        pass

    def remove(self, instance, user):
        pass
