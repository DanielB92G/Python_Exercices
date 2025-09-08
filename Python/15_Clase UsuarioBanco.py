class UsuarioBanco:
    def __init__(self, nombre: str, saldo: float, cuenta_corriente: bool):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad: float):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad: float):
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario origen no tiene suficiente saldo")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad: float):
        self.saldo += cantidad


alicia = UsuarioBanco("Alicia", 100, True)
Jose = UsuarioBanco("Jose", 50, True)

alicia.agregar_dinero(20)         
alicia.transferir_dinero(Jose, 80) 
alicia.retirar_dinero(50)    
print(alicia.saldo, Jose.saldo)
