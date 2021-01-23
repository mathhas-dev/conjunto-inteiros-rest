from rest_framework import viewsets
from rest_framework.response import Response


class BusinessMixin:
    """
    Mixin para adicionar o atributo de classe business_class.
    """

    # Classe a ser instanciada para todos os tipos de serviços de cada model, em cada app.
    business_class = None

    def get_business(self, *args, **kwargs):
        business_class = self.get_business_class()
        return business_class(*args, **kwargs)

    def get_business_class(self):
        assert self.business_class is not None, (
            "'%s' deve incluir um atributo business_class ou "
            "sobrescrever o método get_business_class()."
            % self.__class__.__name__
        )
        return self.business_class


class SimpleEndpoint(BusinessMixin, viewsets.ModelViewSet):
    """
    Classe para componentizar apps
    """

    def get_queryset(self, *args, **kwargs):
        s = self.get_business()
        # Caso esteja buscando objeto simples e exista um método single,
        # utiliza ele, caso contrário, utiliza list.
        if (hasattr(self, 'getting_object') and
            self.getting_object is True and
                hasattr(s, 'single')):
            self.queryset = s.single()
        else:
            self.queryset = s.list()
        return super().get_queryset()

    def get_object(self):
        self.getting_object = True
        obj = super().get_object()
        self.getting_object = False
        return obj

    def create(self, request):
        # Cria nova instância a partir de dados
        service = self.get_business()
        new_instance = service.create(request.data)
        # Serializa nova instância
        serializer = self.get_serializer(new_instance)
        return Response(serializer.data)
