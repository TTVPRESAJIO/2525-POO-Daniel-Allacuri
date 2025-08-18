# inventario.py
from __future__ import annotations
from typing import List, Optional
from producto import Producto

class Inventario:

    def __init__(self) -> None:
        self._productos: List[Producto] = []

    def _existe_id(self, id_busca: int) -> bool:
        return any(p.id == id_busca for p in self._productos)

    def _buscar_por_id(self, id_busca: int) -> Optional[Producto]:
        for p in self._productos:
            if p.id == id_busca:
                return p
        return None

    # ---------- API pública ----------
    def agregar(self, producto: Producto) -> None:
        """Añade un nuevo producto, verificando unicidad de ID."""
        if self._existe_id(producto.id):
            raise ValueError(f"Ya existe un producto con ID {producto.id}.")
        self._productos.append(producto)

    def eliminar_por_id(self, id_eliminar: int) -> bool:
        """Elimina el producto por ID. Retorna True si se eliminó, False si no existía."""
        prod = self._buscar_por_id(id_eliminar)
        if prod:
            self._productos.remove(prod)
            return True
        return False

    def actualizar_por_id(
        self,
        id_objetivo: int,
        *,
        nombre: Optional[str] = None,
        cantidad: Optional[int] = None,
        precio: Optional[float] = None,
    ) -> bool:

        prod = self._buscar_por_id(id_objetivo)
        if not prod:
            return False

        if nombre is not None:
            prod.nombre = nombre
        if cantidad is not None:
            prod.cantidad = cantidad
        if precio is not None:
            prod.precio = precio
        return True

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """Búsqueda parcial y case-insensitive."""
        q = texto.strip().lower()
        return [p for p in self._productos if q in p.nombre.lower()]

    def listar_todos(self) -> List[Producto]:
        """Retorna copia de la lista (para no exponer el interno)."""
        return list(self._productos)

