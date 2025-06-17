class Libro:
    def __init__(self, nombre, autor, codigo):
        self.nombre = nombre
        self.autor = autor
        self.codigo = codigo
        self.disponible= True

    def actualizar_informacion(self, nombre=None, autor=None, codigo=None):
        if nombre:
            self.nombre = nombre
        if autor:
            self.autor = autor
        if codigo:
            self.codigo = codigo

    def mostrar_informacion_libro(self):
        return f"Libro: {self.nombre}, Autor: {self.autor}, Código: {self.codigo}"
