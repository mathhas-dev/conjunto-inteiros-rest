from rest_framework import serializers


class InteiroValidator():
    """
    Classe para validação, atendimento as regras estabeleciddas no enunciado
    """

    def validate(self, data):
        nItens = int(data['nItens'])
        if nItens < 1 or nItens > 1000:
            raise serializers.ValidationError(
                "Quantidade de itens inválida!")

        try:
            lista = list(eval(data['itens']))
        except Exception as e:
            raise serializers.ValidationError(
                "Insira Apenas números entre: 1 e 1000!")

        if nItens != len(lista):
            raise serializers.ValidationError(
                "Quantidade de itens 'K' diferente do específicado em 'N'!")

        lista_tratada = []
        for k in lista:
            if (k >= -1000 and k <= 1000) and (k not in lista_tratada):
                lista_tratada.append(k)

        lista_ordenada = sorted(lista_tratada)
        data['itens'] = str(lista_ordenada)

        data.pop('nItens')
        return data
