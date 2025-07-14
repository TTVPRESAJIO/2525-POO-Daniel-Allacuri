import os


def mostrar_codigo(ruta_script):
    # As1egúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
        '2': 'UNIDAD 1/2.2. Caracteristicas de la POO/2.2-1. Ejemplo - Carro y Acciones.py',
        '3': 'UNIDAD 2/1.1. Tipos de Datos e Identificadores/2.1.1-2 - Ejemplo Identificadores correctos (Python).py',
        '4': 'UNIDAD 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-1 - Ejemplo Clase y Objeto (Coche).py',
        '5': 'UNIDAD 2/1.2. Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo/2.1.2-4 - Ejemplo Polimorfismo (Sobrecarga).py',
        '6': 'UNIDAD 2/2.1. Constructores y Destructores/2.2.1-1 - Uso de constructor.py'
        # Agrega aquí el resto de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()