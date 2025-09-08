from collections import Counter

def contar_palabras(texto: str) -> dict:
    palabras = texto.lower().split()
    return dict(Counter(palabras))

def reemplazar_palabras(texto: str, original: str, nueva: str) -> str:
    return texto.replace(original, nueva)

def eliminar_palabra(texto: str, palabra: str) -> str:
    return " ".join(w for w in texto.split() if w != palabra)

def procesar_texto(texto: str, opcion: str, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Se necesitan 2 argumentos: palabra_original y palabra_nueva")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Se necesita 1 argumento: palabra a eliminar")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opcion no valida")

texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
print(procesar_texto(texto, "contar"))
print(procesar_texto(texto, "reemplazar", "texto", "relato"))
print(procesar_texto(texto, "eliminar", "ejemplo"))
