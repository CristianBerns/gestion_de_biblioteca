# Armamos las funciones para la interfaz de consola

from clases.mascota import Gato, Perro
from clases.cliente import Cliente
from clases.venta import Venta
from clases.inventario import Inventario
from clases.producto import Producto


def registrar_mascota():  # Seria "CREAR" una mascota
    tipo = input("Ingrese el tipo de mascota (Gato/Perro):").strip().lower()
    nombre = input("Ingrese el nombre: ").strip().lower()
    edad = int(input("Edad de la mascota: "))
    salud = input("Estado de la salud de la mascota: ").strip().lower()
    precio = float(input("Precio de atención de la mascota: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        nivel_de_energía = input("Nivel de energía del perrro")
        mascota = Perro(
            nombre, edad, salud, precio, raza, nivel_de_energía
        )  # Acá instanciamo
    elif tipo == "gato":
        raza = input("Raza del gato: ")
        independencia = input("Nivel de independencia del gato")
        mascota = Gato(
            nombre, edad, salud, precio, raza, independencia
        )  # Acá instanciamos la mascota
    else:
        print("Tipo de mascota no reconocida")

    return mascota


def registrar_cliente():  # Sería "CREAR" un cliente
    nombre = input("Ingrese el nombre del cliente: ").strip().lower()
    direccion = input("Ingrese la direccion del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)  # Acá se instancia al cliente
    return cliente


def registrar_producto():  # Sería "CREAR" un producto
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto


def registar_venta(clientes, inventario):  # Sería "CREAR" una venta
    nombre_cliente = input(
        "Nombre del cliente : "
    )  # Es el cliente a buscar dentro de la lista de clientes
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return

    productos = []

    while True:
        nombre_del_producto = input("Nombre del producto (deje vacío para finalizar)")
        if not nombre_del_producto:
            break
        producto = next(
            (
                p
                for p in inventario.lista_de_productos
                if p.nombre == nombre_del_producto
            ),
            None,
        )
        if producto:
            productos.append(producto)
        else:
            print("Procucto no encontrado")
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta
        print("La venta ha sido registrada con éxito")
    else:
        print("No se han registrado productos para la venta")


def mostrar_menu():
    print("n\ Menú de gestión")
    print("1. Registrar mascota")
    print("2. Registrar cliente")
    print("3. Registrar producto")
    print("4. Registar venta")
    print("5. Mostrar información acerca de mascotas")
    print("6. Mostrar información acerca de productos")
    print("7. Mostrar información acerca de clientes")
    print("8. Generar alerta de inventario")
    print("9. Salir")


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada")

        elif opcion == input("2"):
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado")

        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Procuto registrado")

        elif opcion == "4":
            registar_venta(clientes, inventario)

        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caractaristicas())

        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())

        elif opcion == "6":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_informacion())

        elif opcion == "8":
            umbral_minimo = int(input("Ingrese el umbral minimo del inventario: "))
            print(inventario.generar_alerta(umbral_minimo))

        elif opcion == 9:
            print("Saliendo del sistema")
            break
        else:
            print("Opción no válida, intente nuevamnete")


if (
    __name__ == "__main__"
):  # Esto hace que este programa solo se ejecute desde este archivo
    main()
