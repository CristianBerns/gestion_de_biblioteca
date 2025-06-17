from matplotlib.testing import set_font_settings_for_testing


class Cliente:
    def __init__(self, nombre, direccion, telefono):  # Inicio el construcctor
        self.nombre = nombre  # Hago la
        self.direccion = direccion  # asignación de
        self.telefono = telefono  # las características
        self.historial_compras = (
            []
        )  # Este parametro no está dentro del constructor. Se inicia vacío

    def actualizar_informacion(
        self, direccion=None, telefono=None
    ):  # Si no actualizo, quedan los mismos valores, de ahí el None
        if direccion:  # Esto lo uso para actualizar información
            self.direccion = direccion
        if telefono:
            self.telefono = telefono

    def registrar_compra(
        self, compra
    ):  # Es otro método de Cliente, al igual que el de arriba
        self.historial_compras.append(compra)

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}, Telefóno: {self.telefono}"
