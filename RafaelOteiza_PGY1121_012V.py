import numpy as np
import os

precios_venta = {
    'Platinum': 120000,
    'Gold': 80000,
    'Silver': 50000,
}
asientos = [
    ["01","02","03","04","05","06","07","08","09","10"],
    ["11","12","13","14","15","16","17","18","19","20"],
    ["21","22","23","24","25","26","27","28","29","30"],
    ["31","32","33","34","35","36","37","38","39","40"],
    ["41","42","43","44","45","46","47","48","49","50"],
    ["51","52","53","54","55","56","57","58","59","60"],
    ["61","62","63","64","65","66","67","68","69","70"],
    ["71","72","73","74","75","76","77","78","79","80"],
    ["81","82","83","84","85","86","87","88","89","90"],
    ["91","92","93","94","95","96","97","98","99","110"],
]

np.entradas_ocupadas = []
todas_entradas = []

def imprimir_asientos():
    os.system("cls")
    sala = "-----------------------------------------Asientos----------------------------------------------\n"
    for i in asientos:
        for x in i:
            todas_entradas.append(x)
            if x in np.entradas_ocupadas:
                sala += ocupado(f"[ {x} ]")
            else:
                sala += disponible(f"[ {x} ]")
        sala += "\n"
    return sala

filas = 10
columnas = 10

entradas_disponibles = [[True] * columnas for _ in range(filas)]

compradores = []

def mostrar_menu():
    print("----- Creativos.cl -----")
    print("- Entradas VIP Michael Jam -")
    print("1. Comprar entrada")
    print("2. Mostrar entradas disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def comprar_entrada():
    global entradas_disponibles
    print("----- Comprar Entrada -----")
    print(imprimir_asientos())

    cantidad_entradas = obtener_cantidad_entradas()
    if cantidad_entradas == 0:
        print("No se ha realizado la compra de entradas.")
        return

    for _ in range(cantidad_entradas):
        vali = True
        while vali:
            try:
                print("Los asientos reservados aparecen en color rojo")
                asiento = input("Seleccione el asiento que desea comprar: ")
                if asiento in todas_entradas:
                    if asiento not in np.entradas_ocupadas:
                        np.entradas_ocupadas.append(asiento)
                        vali = False
                    else:
                        print(f"El asiento {asiento} que desea comprar no está disponible.")
                else:
                    print(f"El asiento {asiento} que desea comprar no existe.")
                    input("Presione enter para continuar: ")
            except ValueError:
                print("Opción ingresada inválida.")

        fila = (int(asiento) - 1) // 10
        columna = (int(asiento) - 1) % 10

        if not entradas_disponibles[fila][columna]:
            print("\033[0;31mEntrada no disponible.\033[0m")
            continue

        tipo_entrada = ''
        if 1 <= int(asiento) <= 20:
            tipo_entrada = 'Platinum'
        elif 21 <= int(asiento) <= 50:
            tipo_entrada = 'Gold'
        elif 51 <= int(asiento) <= 100:
            tipo_entrada = 'Silver'
        else:
            print("Tipo de entrada inválida.")
            continue

        entrada = tipo_entrada + ' ' + asiento

        entradas_disponibles[fila][columna] = False

        # Validar y almacenar los datos del comprador
        nombre = validacion_nombre()
        apellido = validacion_apellido()
        rut = validacion_rut()
        telefono = validacion_telefono()

        compradores.append({'nombre': nombre, 'apellido': apellido, 'rut': rut, 'telefono': telefono, 'entrada': entrada})
        print("Compra realizada correctamente.")

def obtener_cantidad_entradas():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas que desea comprar (1-3): "))
            if 1 <= cantidad <= 3:
                return cantidad
            else:
                print("La cantidad de entradas ingresada no es válida. Intente nuevamente.")
        except ValueError:
            print("Opción ingresada inválida. Intente nuevamente.")

def validacion_nombre():        
    vali = True
    while vali:
        nombre = input("Ingrese su nombre: ")
        if 3 <= len(nombre) <= 15:
            input("Nombre ingresado correctamente. Presione enter para continuar: ")
            vali = False
        else: 
            print("El nombre ingresado es inválido")
    return nombre

def validacion_apellido():
    vali = True
    while vali:
        apellido = input("Ingrese su apellido: ")
        if 3 <= len(apellido) <= 15:
            input("Apellido ingresado correctamente. Presione enter para continuar: ")  
            vali = False
        else: 
            print("El apellido ingresado es inválido")
    return apellido

def validacion_rut():
    vali = True
    while vali:
        rut = input("Ingrese su rut como el siguiente ejemplo (19498852): ")
        if 0 < len(rut) < 9:
            input("Rut ingresado correctamente. Presione enter para continuar: ")
            vali = False
        else: 
            print("El rut ingresado es incorrecto")
    return rut

def validacion_telefono():
    vali = True
    while vali:
        telefono = input("Ingrese el teléfono (Ejemplo: 984494726): ")
        if 0 < len(telefono) < 10:
            input("Teléfono ingresado correctamente. Presione enter para continuar: ")
            vali = False
        else: 
            print("El teléfono ingresado es incorrecto")
    return telefono

def ocupado(texto):
    return f"\033[0;31m[ X ]\033[0m"

def disponible(texto):
    return f"{texto}"

def mostrar_listado_compradores():
    print("----- Listado de compradores -----")
    compradores_ordenados = sorted(compradores, key=lambda x: x['rut'])
    for comprador in compradores_ordenados:
        print(f"Nombre: {comprador['nombre']}, Apellido: {comprador['apellido']}, Rut: {comprador['rut']}, Teléfono: {comprador['telefono']}, Entrada: {comprador['entrada']}")

def mostrar_ganancias_totales():
    print("----- Ganancias totales -----")
    total_ventas = 0
    ventas_por_tipo = {}

    for entrada in compradores:
        tipo_entrada = entrada['entrada'].split()[0]
        if tipo_entrada in precios_venta and entrada['entrada']:
            if tipo_entrada in ventas_por_tipo:
                ventas_por_tipo[tipo_entrada] += 1
            else:
                ventas_por_tipo[tipo_entrada] = 1

            total_ventas += precios_venta[tipo_entrada]

    print("Tipo Entrada\tValor\t\tCantidad\tTotal")
    for tipo_entrada, cantidad_vendida in sorted(ventas_por_tipo.items()):
        valor_entrada = precios_venta[tipo_entrada]
        total_entrada = valor_entrada * cantidad_vendida
        print(f"{tipo_entrada.ljust(15)}\t${str(valor_entrada).ljust(7)}\t\t{str(cantidad_vendida).ljust(8)}\t${total_entrada}")

    print(f"\nVentas totales: ${total_ventas}")


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            comprar_entrada()
        elif opcion == '2':
            print(imprimir_asientos())
            input("Presione enter para continuar: ")
        elif opcion == '3':
            mostrar_listado_compradores()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            print("¡Gracias por utilizar el sistema!")
            print("Versión 2.0")
            print("Rafael Oteiza")
            print("13-07-2023")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()
