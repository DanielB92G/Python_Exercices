def encontrar_puesto_empleado(nombre_completo: str, empleados: list[dict]) -> str:
    partes = nombre_completo.strip().split()
    if len(partes) < 2:
        return "Formato esperado: 'Nombre Apellido'"
    nombre, apellido = partes[0], " ".join(partes[1:])
    for emp in empleados:
        if emp.get("nombre") == nombre and emp.get("apellido") == apellido:
            return emp.get("puesto", "Puesto no informado")
    return f"{nombre_completo} no trabaja aquí."


empleados = [
    {'nombre': "Daniel", 'apellido': "Bedoya", 'puesto': "Ingeniero Industrial"},
    {'nombre': "David", 'apellido': "Bedoya", 'puesto': "Product Manager"},
    {'nombre': "Gloria", 'apellido': "Coloma", 'puesto': "Marketing"},
]

print(encontrar_puesto_empleado("Daniel Bedoya", empleados)) 
print(encontrar_puesto_empleado("Jaime Serrano", empleados))      
