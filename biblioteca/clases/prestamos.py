from datetime import datetime


class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        self.fecha_prestamo = datetime.now()
        self.libro_disponible = True

    def mostrar_informacion(self):
        fecha_devolucion = (
            self.fecha_devolucion if fecha_devolucion else "No se ha devuelto el libro"
        )
        return f"Usuario {self.usuario}, Libro: {self.libro}, Fecha del préstamo:{self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}"
