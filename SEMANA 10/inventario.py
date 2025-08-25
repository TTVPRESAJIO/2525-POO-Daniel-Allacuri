# inventario.py
from __future__ import annotations
from producto import Producto
from typing import List, Optional

ARCHIVO = "inventario.txt"

class Inventario:
    def __init__(self):
        self._productos: List[Producto] = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open(ARCHIVO, "w", encoding="utf-8") as f:
                for p in self._productos:
                    f.write(p.to_linea() + "\n")
        except PermissionError:
            print("✗ Error: no se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"✗ Error inesperado al guardar: {e}")

    def cargar_desde_archivo(self):
        #Lee productos del archivo y los carga en memoria
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        prod = Producto.from_linea(linea)
                        self._productos.append(prod)
                    except Exception:
                        print(f"✗ Línea inválida en archivo: {linea.strip()}")
        except FileNotFoundError:
            # Si no existe, lo crea vacío
            try:
                with open(ARCHIVO, "w", encoding="utf-8") as _: pass
                print("⚠ Archivo inventario.txt no existía, se creó vacío.")
            except Exception as e:
                print(f"✗ No se pudo crear inventario.txt: {e}")
        except PermissionError:
            print("✗ Error: no se tienen permisos para leer inventario.txt.")

    # ---------------- CRUD ----------------
    def agregar(self, p: Producto):
        if any(prod.id == p.id for prod in self._productos):
            raise ValueError(f"Ya existe un producto con ID {p.id}")
        self._productos.append(p)
        self.guardar_en_archivo()

    def eliminar_por_id(self, id_: int) -> bool:
        for prod in self._productos:
            if prod.id == id_:
                self._productos.remove(prod)
                self.guardar_en_archivo()
                return True
        return False

    def actualizar_por_id(self, id_: int, *, nombre=None, cantidad=None, precio=None) -> bool:
        for prod in self._productos:
            if prod.id == id_:
                if nombre: prod.nombre = nombre
                if cantidad is not None: prod.cantidad = cantidad
                if precio is not None: prod.precio = precio
                self.guardar_en_archivo()
                return True
        return False

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        q = texto.strip().lower()
        return [p for p in self._productos if q in p.nombre.lower()]

    def listar_todos(self) -> List[Producto]:
        return list(self._productos)
