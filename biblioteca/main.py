from funciones import (
    registrar_usuario,
    registrar_libro,
    registrar_prestamo,
    registro_de_devolucion
)

def mostrar_menu():
    print("\n--- Menú de Gestión de Biblioteca ---")
    print("1. Registrar un libro")
    print("2. Crear un usuario")
    print("3. Pedir un préstamo")
    print("4. Realizar una devolución")
    print("5. Ver información de libros")
    print("6. Ver información de usuarios")
    print("7. Salir")

def main():
    libros = []
    usuarios = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro = registrar_libro()
            if libro:
                libros.append(libro)
                print("Libro registrado con éxito.")
        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("Usuario registrado con éxito.")
        elif opcion == "3":
            registrar_prestamo(usuarios, libros)
        elif opcion == "4":
            registro_de_devolucion(usuarios, libros)
        elif opcion == "5":
            for libro in libros:
                print(libro.mostrar_informacion_libro())
        elif opcion == "6":
            for usuario in usuarios:
                print(usuario.mostrar_informacion_usuario())  # Acá corregí el nombre del método
                for prestamo in usuario.prestamos:
                    print(prestamo.mostrar_informacion())
        elif opcion == "7":
            print("Hasta luego.")
            break
        else:
            print("Seleccione una opción válida del menú")

if __name__ == "__main__":
    main()
