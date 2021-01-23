from core.resource import SimpleEndpoint
from inteiros.models import Inteiro
from inteiros.serializers import InteiroSerializer
from inteiros.business import InteiroService


class InteiroViewSet(SimpleEndpoint):
    """
    Camada View (endpoints) do conjunto dos inteiros
    """
    serializer_class = InteiroSerializer
    business_class = InteiroService
