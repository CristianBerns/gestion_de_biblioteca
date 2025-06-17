from datetime import datetime


class Venta:
    def __init__(self, cliente, lista_de_productos):
        self.cliente = cliente
        self.lista_de_productos = lista_de_productos
        self.fecha = datetime.now()
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio for producto in self.lista_de_productos)

    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta registrada: {self.mostrar_informacion()}"

    def mostrar_informacion(self):
        productos = ", ".join(
            [producto.nombre for producto in self.lista_de_productos]
        )  # Las comas son para indicar que la sepaaración va a ser por esos carácteres
        return (
            f"Cleinte: {self.cliente.nombre}, Producto {productos}, Total: {self.total}"
        )
