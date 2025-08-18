# app.py
from __future__ import annotations
from inventario import Inventario
from producto import Producto

def pedir_entero(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        try:
            valor = int(dato)
            return valor
        except ValueError:
            print("→ Debe ser un número entero. Intenta de nuevo.")

def pedir_flotante(mensaje: str) -> float:
    while True:
        dato = input(mensaje).strip()
        try:
            valor = float(dato)
            return valor
        except ValueError:
            print("→ Debe ser un número (usa punto decimal). Intenta de nuevo.")

def pedir_no_vacio(mensaje: str) -> str:
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("→ No puede estar vacío. Intenta de nuevo.")

# -------- Operaciones del menú --------
def opcion_agregar(inv: Inventario) -> None:
    print("\n=== Agregar producto ===")
    id_ = pedir_entero("ID (entero, único): ")
    nombre = pedir_no_vacio("Nombre: ")
    cantidad = pedir_entero("Cantidad (entero ≥ 0): ")
    precio = pedir_flotante("Precio (≥ 0): ")
    try:
        p = Producto(id_, nombre, cantidad, precio)
        inv.agregar(p)
        print("✓ Producto agregado.")
    except (ValueError, TypeError) as e:
        print(f"✗ No se pudo agregar: {e}")

def opcion_eliminar(inv: Inventario) -> None:
    print("\n=== Eliminar producto ===")
    id_ = pedir_entero("ID a eliminar: ")
    if inv.eliminar_por_id(id_):
        print("✓ Producto eliminado.")
    else:
        print("✗ No existe un producto con ese ID.")

def opcion_actualizar(inv: Inventario) -> None:
    print("\n=== Actualizar producto ===")
    id_ = pedir_entero("ID a actualizar: ")
    print("Deja en blanco lo que no quieras cambiar.")
    nuevo_nombre = input("Nuevo nombre: ").strip()
    nueva_cant = input("Nueva cantidad: ").strip()
    nuevo_precio = input("Nuevo precio: ").strip()

    kw = {}
    if nuevo_nombre:
        kw["nombre"] = nuevo_nombre
    if nueva_cant:
        try:
            kw["cantidad"] = int(nueva_cant)
        except ValueError:
            print("→ Cantidad ignorada (no es entero).")
    if nuevo_precio:
        try:
            kw["precio"] = float(nuevo_precio)
        except ValueError:
            print("→ Precio ignorado (no es numérico).")

    if not kw:
        print("Nada para actualizar.")
        return

    try:
        ok = inv.actualizar_por_id(id_, **kw)
        if ok:
            print("✓ Producto actualizado.")
        else:
            print("✗ No existe un producto con ese ID.")
    except (ValueError, TypeError) as e:
        print(f"✗ Error al actualizar: {e}")

def opcion_buscar(inv: Inventario) -> None:
    print("\n=== Buscar por nombre ===")
    q = pedir_no_vacio("Texto de búsqueda: ")
    resultados = inv.buscar_por_nombre(q)
    if resultados:
        print(f"✓ {len(resultados)} resultado(s):")
        imprimir_tabla(resultados)
    else:
        print("Sin coincidencias.")

def opcion_listar(inv: Inventario) -> None:
    print("\n=== Inventario completo ===")
    productos = inv.listar_todos()
    if productos:
        imprimir_tabla(productos)
    else:
        print("Inventario vacío.")

# -------- Presentación --------
def imprimir_tabla(productos) -> None:
    # Presentación tipo tabla simple
    print(f"{'ID':>4}  {'Nombre':<30}  {'Cantidad':>8}  {'Precio':>10}")
    print("-" * 60)
    for p in productos:
        print(f"{p.id:>4}  {p.nombre:<30}  {p.cantidad:>8}  {p.precio:>10.2f}")

# -------- Menú principal --------
def main() -> None:
    inv = Inventario()

    #  Datos de ejemplo para probar rápido:
    for demo in [
        (1, "Café isntantaneo", 10, 4.5),
        (2, "Azucar 1kg", 25, 3.2),
        (3, "Sal fina 4kg", 5, 2.9),
    ]:
        try:
            inv.agregar(Producto(*demo))
        except Exception:
            pass

    while True:
        print("\n===== GESTIÓN DE INVENTARIO =====")
        print("1) Agregar producto")
        print("2) Eliminar por ID")
        print("3) Actualizar (nombre / cantidad / precio) por ID")
        print("4) Buscar por nombre")
        print("5) Mostrar todos")
        print("0) Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            opcion_agregar(inv)
        elif opcion == "2":
            opcion_eliminar(inv)
        elif opcion == "3":
            opcion_actualizar(inv)
        elif opcion == "4":
            opcion_buscar(inv)
        elif opcion == "5":
            opcion_listar(inv)
        elif opcion == "0":
            print("Saliendo… ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
