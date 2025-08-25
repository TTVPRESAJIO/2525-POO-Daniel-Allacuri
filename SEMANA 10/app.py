# app.py
from inventario import Inventario
from producto import Producto

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("✗ Debes ingresar un número entero.")

def pedir_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("✗ Debes ingresar un número decimal.")

def pedir_no_vacio(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato: return dato
        print("✗ No puede estar vacío.")

def imprimir_tabla(productos):
    print(f"{'ID':>4} | {'Nombre':<25} | {'Cantidad':>8} | {'Precio':>8}")
    print("-" * 55)
    for p in productos:
        print(f"{p.id:>4} | {p.nombre:<25} | {p.cantidad:>8} | {p.precio:>8.2f}")

def main():
    inv = Inventario()

    while True:
        print("\n===== GESTIÓN DE INVENTARIO =====")
        print("1) Agregar producto")
        print("2) Eliminar producto por ID")
        print("3) Actualizar producto por ID")
        print("4) Buscar producto por nombre")
        print("5) Listar todos")
        print("0) Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            id_ = pedir_entero("ID único: ")
            nombre = pedir_no_vacio("Nombre: ")
            cantidad = pedir_entero("Cantidad: ")
            precio = pedir_flotante("Precio: ")
            try:
                inv.agregar(Producto(id_, nombre, cantidad, precio))
                print("✓ Producto agregado y guardado en inventario.txt")
            except Exception as e:
                print(f"✗ Error al agregar: {e}")

        elif opcion == "2":
            id_ = pedir_entero("ID a eliminar: ")
            if inv.eliminar_por_id(id_):
                print("✓ Producto eliminado del inventario y archivo.")
            else:
                print("✗ No se encontró el producto.")

        elif opcion == "3":
            id_ = pedir_entero("ID a actualizar: ")
            nuevo_nombre = input("Nuevo nombre (enter para no cambiar): ").strip()
            nueva_cant = input("Nueva cantidad (enter para no cambiar): ").strip()
            nuevo_precio = input("Nuevo precio (enter para no cambiar): ").strip()
            cambios = {}
            if nuevo_nombre: cambios["nombre"] = nuevo_nombre
            if nueva_cant:
                try: cambios["cantidad"] = int(nueva_cant)
                except: pass
            if nuevo_precio:
                try: cambios["precio"] = float(nuevo_precio)
                except: pass
            if inv.actualizar_por_id(id_, **cambios):
                print("✓ Producto actualizado y guardado.")
            else:
                print("✗ No se encontró el producto.")

        elif opcion == "4":
            q = pedir_no_vacio("Texto a buscar: ")
            res = inv.buscar_por_nombre(q)
            if res: imprimir_tabla(res)
            else: print("✗ Sin coincidencias.")

        elif opcion == "5":
            prods = inv.listar_todos()
            if prods: imprimir_tabla(prods)
            else: print("Inventario vacío.")

        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("✗ Opción inválida.")

if __name__ == "__main__":
    main()
