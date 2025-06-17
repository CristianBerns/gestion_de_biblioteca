class Usuario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.prestamos = []

    def actaulizar_informacion_usuario(
        self, nombre=None, direccion=None, telefono=None
    ):
        if nombre:
            self.nombre = nombre
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def prestamos_realizados(self, presstamo):
        self.prestamos.append(presstamo)

    def mostrar_informacion_usuario(self):
        return f"Usuario: {self.nombre}, Dirección: {self.direccion}, Telefóno: {self.telefono}"
