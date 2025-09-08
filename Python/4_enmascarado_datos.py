def enmascarado_datos(valor) -> str:
    s = str(valor)
    return s if len(s) <= 4 else "#" * (len(s) - 4) + s[-4:]


print(enmascarado_datos("123456789")) 
print(enmascarado_datos(9876))         
