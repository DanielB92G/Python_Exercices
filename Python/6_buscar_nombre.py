def buscar_nombre(lista_nombres: list[str], nombre: str) -> None:
    if nombre in lista_nombres:
        print(f"{nombre} fue encontrado en la lista.")
    else:
        raise LookupError(f"{nombre} no está en la lista.")

# Caso de uso
nombres = ["Daniel", "Gloria", "Carmen"]
try:
    buscar_nombre(nombres, "Gloria") 
    buscar_nombre(nombres, "Carmen")   
except LookupError as e:
    print("Error:", e)
