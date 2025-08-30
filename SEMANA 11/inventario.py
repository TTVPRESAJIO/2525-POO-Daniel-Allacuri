# inventario.py
from __future__ import annotations
import json
from typing import Dict, List, Set
from producto import Producto

ARCHIVO_JSON = "inventario.json"


class Inventario:

    def __init__(self) -> None:
        self._items: Dict[int, Producto] = {}
        self._nombres_idx: Set[str] = set()   # índice de nombres (en minúsculas)
        self.cargar()

    def guardar(self) -> None:

        data = [p.a_dict() for p in self._items.values()]
        try:
            with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except PermissionError:
            print("✗ Permiso denegado al escribir el archivo de inventario.")
        except OSError as e:
            print(f"✗ Error de E/S al guardar inventario: {e}")

    def cargar(self) -> None:

        try:
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Formato inválido en inventario.json")

            self._items.clear()
            self._nombres_idx.clear()
            for row in data:
                try:
                    p = Producto.desde_dict(row)
                    self._items[p.id] = p
                    self._nombres_idx.add(p.nombre.lower())
                except Exception:
                    print(f"⚠ Registro inválido omitido: {row}")

        except FileNotFoundError:
            try:
                with open(ARCHIVO_JSON, "w", encoding="utf-8") as f:
                    json.dump([], f)
                print("ℹ inventario.json no existía. Se creó vacío.")
            except OSError as e:
                print(f"✗ No se pudo crear inventario.json: {e}")

        except json.JSONDecodeError as e:
            print(f"✗ inventario.json corrupto ({e}). Se cargará vacío.")
        except PermissionError:
            print("✗ Permiso denegado al leer inventario.json.")
        except OSError as e:
            print(f"✗ Error de E/S al leer inventario: {e}")

    def agregar(self, p: Producto) -> None:
        if p.id in self._items:
            raise ValueError(f"Ya existe un producto con ID {p.id}.")
        self._items[p.id] = p
        self._nombres_idx.add(p.nombre.lower())
        self.guardar()

    def eliminar_por_id(self, id_: int) -> bool:
        prod = self._items.pop(id_, None)
        if prod is None:
            return False
        self._nombres_idx = {x.nombre.lower() for x in self._items.values()}
        self.guardar()
        return True

    def actualizar_por_id(self, id_: int, *, nombre=None, cantidad=None, precio=None) -> bool:
        prod = self._items.get(id_)
        if prod is None:
            return False

        if nombre is not None:
            self._nombres_idx.discard(prod.nombre.lower())
            prod.nombre = nombre
            self._nombres_idx.add(prod.nombre.lower())
        if cantidad is not None:
            prod.cantidad = cantidad
        if precio is not None:
            prod.precio = precio

        self.guardar()
        return True

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        q = texto.strip().lower()
        if not q:
            return []
        return [p for p in self._items.values() if q in p.nombre.lower()]

    def listar_todos(self) -> List[Producto]:
        return list(self._items.values())

    def nombres_unicos(self) -> Set[str]:
        return set(self._nombres_idx)

    def snapshot_tuplas(self) -> List[tuple]:
        return [p.a_tuple() for p in self._items.values()]
