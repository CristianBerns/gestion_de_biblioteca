from clases.libros import Libro
from clases.prestamos import Prestamo
from clases.usuarios import Usuario

usuarios = []
libros = []

def registrar_libro():
    nombre = input("Ingrese el nombre del libro: ").strip().lower()
    autor = input("Ingrese el autor del libro: ").strip().lower()
    codigo = int(input("Inserte el código del libro: "))
    libro = Libro(nombre, autor, codigo)
    libros.append(libro)
    print("Libro registrado con éxito.")
    return libro

def registrar_usuario():
    nombre = input("Ingrese el nombre del usuario: ").strip().lower()
    direccion = input("Ingrese la dirección: ").strip().lower()
    telefono = input("Ingrese el teléfono: ")
    usuario = Usuario(nombre, direccion, telefono)
    usuarios.append(usuario)
    print("Usuario registrado con éxito.")
    return usuario

def registrar_prestamo(usuarios,libros):
    nombre_usuario = input("Ingrese el nombre del usuario: ").strip().lower()
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no encontrado.")
        return

    nombre_libro = input("Ingrese el nombre del libro: ").strip().lower()
    libro = next((l for l in libros if l.nombre == nombre_libro), None)
    if not libro:
        print("Libro no encontrado.")
        return

    if not libro.disponible:
        print("El libro ya está prestado.")
        return

    prestamo = Prestamo(libro, usuario)
    usuario.registrar_prestamo(prestamo)
    libro.disponible = False
    print("Préstamo registrado con éxito.")

def registro_de_devolucion():
    nombre_usuario = input("Ingrese el nombre del usuario: ").strip().lower()
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("Usuario no encontrado.")
        return

    nombre_libro = input("Ingrese el nombre del libro a devolver: ").strip().lower()
    prestamo = next((p for p in usuario.prestamos if p.libro.nombre == nombre_libro), None)

    if not prestamo:
        print("Ese libro no figura como prestado por el usuario.")
        return

    prestamo.libro.disponible = True
    print(f"Libro '{prestamo.libro.nombre}' devuelto con éxito.")
