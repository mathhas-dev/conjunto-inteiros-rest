from django.db import models
from django.core.validators import int_list_validator


class Inteiro(models.Model):
    itens = models.CharField(validators=[int_list_validator], max_length=1001)
