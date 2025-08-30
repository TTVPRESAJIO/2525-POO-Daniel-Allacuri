# app.py
from inventario import Inventario
from producto import Producto


def pedir_entero(msg: str) -> int:
    while True:
        dato = input(msg).strip()
        try:
            return int(dato)
        except ValueError:
            print("→ Debe ser un número entero.")

def pedir_flotante(msg: str) -> float:
    while True:
        dato = input(msg).strip()
        try:
            return float(dato)
        except ValueError:
            print("→ Debe ser un número (usa punto).")

def pedir_texto(msg: str) -> str:
    while True:
        dato = input(msg).strip()
        if dato:
            return dato
        print("→ No puede estar vacío.")


def imprimir_tabla(productos) -> None:
    print(f"{'ID':>4}  {'Nombre':<30}  {'Cantidad':>8}  {'Precio':>10}")
    print("-" * 60)
    for p in productos:
        print(f"{p.id:>4}  {p.nombre:<30}  {p.cantidad:>8}  {p.precio:>10.2f}")

def main() -> None:
    inv = Inventario()

    while True:
        print("\n===== INVENTARIO (POO + COLECCIONES + ARCHIVO) =====")
        print("1) Agregar producto")
        print("2) Eliminar por ID")
        print("3) Actualizar por ID")
        print("4) Buscar por nombre")
        print("5) Mostrar todos")
        print("6) Ver nombres únicos (set)")
        print("7) Ver snapshot (tuplas)")
        print("0) Salir")
        op = input("Elige una opción: ").strip()

        if op == "1":
            try:
                id_ = pedir_entero("ID único: ")
                nombre = pedir_texto("Nombre: ")
                cant = pedir_entero("Cantidad (>= 0): ")
                precio = pedir_flotante("Precio (>= 0): ")
                prod = Producto(id_, nombre, cant, precio)
                inv.agregar(prod)
                print("✓ Producto agregado y guardado en inventario.json")
            except Exception as e:
                print(f"✗ No se pudo agregar: {e}")

        elif op == "2":
            id_ = pedir_entero("ID a eliminar: ")
            if inv.eliminar_por_id(id_):
                print("✓ Producto eliminado y archivo actualizado.")
            else:
                print("✗ No existe un producto con ese ID.")

        elif op == "3":
            id_ = pedir_entero("ID a actualizar: ")
            print("Deja vacío lo que no quieras cambiar.")
            n = input("Nuevo nombre: ").strip()
            c = input("Nueva cantidad: ").strip()
            pr = input("Nuevo precio: ").strip()

            cambios = {}
            if n:
                cambios["nombre"] = n
            if c:
                try:
                    cambios["cantidad"] = int(c)
                except ValueError:
                    print("↪ Cantidad ignorada (no es entero).")
            if pr:
                try:
                    cambios["precio"] = float(pr)
                except ValueError:
                    print("↪ Precio ignorado (no es numérico).")

            if not cambios:
                print("↪ Nada para actualizar.")
            else:
                if inv.actualizar_por_id(id_, **cambios):
                    print("✓ Producto actualizado y guardado.")
                else:
                    print("✗ No existe un producto con ese ID.")

        elif op == "4":
            q = pedir_texto("Texto de búsqueda: ")
            res = inv.buscar_por_nombre(q)
            if res:
                imprimir_tabla(res)
            else:
                print("Sin coincidencias.")

        elif op == "5":
            todos = inv.listar_todos()
            if todos:
                imprimir_tabla(todos)
            else:
                print("Inventario vacío.")

        elif op == "6":
            nombres = inv.nombres_unicos()
            if nombres:
                print("Nombres únicos (normalizados):")
                for nom in sorted(nombres):
                    print(" -", nom)
            else:
                print("No hay nombres registrados.")

        elif op == "7":

            snap = inv.snapshot_tuplas()
            if snap:
                print("(id, nombre, cantidad, precio)")
                for t in snap:
                    print(t)
            else:
                print("Inventario vacío.")

        elif op == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
