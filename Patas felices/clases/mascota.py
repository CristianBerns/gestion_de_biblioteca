class Mascota:
    def __init__(self, nombre, edad, salud, precio):  # Creo el constructor de la clase
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_información(
        self, edad=None, salud=None, precio=None
    ):  # Es un método de la clase Mascota
        if edad:
            self.edad = edad  # Por defecto cada uno de estos tres valores era None, pero si quiero actualizar
        if salud:  # alguno, lo coloco acá y se actualiza
            self.salud = salud  # Si no lo mandamos, simplemente no se actualizar
        if precio:
            self.precio = precio

    def mostrar_información(self):  # Al poner self, hacemos que esté la instancia
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"


class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, nivel_de_energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.nivel_de_energia = nivel_de_energia

    def mostrar_caracteristicas(self):  # Es un método propio de la clase Perro
        return f"Raza: {self.raza}, Nivel de energia{self.nivel_de_energia}"


class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia

    def mostrar_caractaristicas(self):  # Este es un método de la clase Gato
        return f"Raza: {self.raza}, Independencia: {self.independencia}"
