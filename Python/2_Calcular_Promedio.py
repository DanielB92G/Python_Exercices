def calcular_promedio(numeros: list[float]) -> float:
    if not numeros:
        raise ValueError("La lista está vacía")
    return sum(numeros) / len(numeros)

print(calcular_promedio([20, 6, 7]))
