# Algoritmo básico, respondendo ao enunciado através da console

try:
    qtd = int(input())
    if qtd >= 1 and qtd <= 1000:
        lista = []

        for n in range(qtd):
            try:
                k = int(input())
            except Exception as e:
                print("ERRO: " + str(e))
            if k >= -1000 and k <= 1000 and k not in lista:
                lista.append(k)

        listaOrdenada = sorted(lista)
        for n in listaOrdenada:
            print(n)

except Exception as e:
    print("Insira Apenas números entre: 1 e 1000!")
