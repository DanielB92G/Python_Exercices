numeros_pares = lambda lista: list(filter(lambda x: isinstance(x, int) and x % 2 == 0, lista))


lista_numeros = [24, 56, 2.3, 19, -1, 0]
print(numeros_pares(lista_numeros))  
