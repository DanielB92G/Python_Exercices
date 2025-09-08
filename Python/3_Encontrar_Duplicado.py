def encontrar_duplicado(items: list) -> object | None:
    vistos = set()
    for x in items:
        if x in vistos:
            return x
        vistos.add(x)
    return None


print(encontrar_duplicado([3, 1, 4, 1, 5, 9]))  
print(encontrar_duplicado([1, 2, 3]))           
