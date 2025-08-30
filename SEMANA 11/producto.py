# producto.py
from __future__ import annotations
from typing import Dict, Tuple


class Producto:
    def __init__(self, id: int, nombre: str, cantidad: int, precio: float) -> None:
        self._id = self._validar_id(id)
        self._nombre = self._validar_nombre(nombre)
        self._cantidad = self._validar_cantidad(cantidad)
        self._precio = self._validar_precio(precio)

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precio(self) -> float:
        return self._precio

    @id.setter
    def id(self, _nuevo: int) -> None:
        # el ID no se cambia para mantener unicidad en inventario
        raise AttributeError("El ID no puede modificarse una vez creado.")

    @nombre.setter
    def nombre(self, nuevo: str) -> None:
        self._nombre = self._validar_nombre(nuevo)

    @cantidad.setter
    def cantidad(self, nueva: int) -> None:
        self._cantidad = self._validar_cantidad(nueva)

    @precio.setter
    def precio(self, nuevo: float) -> None:
        self._precio = self._validar_precio(nuevo)

    def a_dict(self) -> Dict:
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio,
        }

    @staticmethod
    def desde_dict(data: Dict) -> "Producto":
        return Producto(
            id=int(data["id"]),
            nombre=str(data["nombre"]),
            cantidad=int(data["cantidad"]),
            precio=float(data["precio"]),
        )

    def a_tuple(self) -> Tuple[int, str, int, float]:
        return (self._id, self._nombre, self._cantidad, self._precio)

    def __repr__(self) -> str:
        return (f"Producto(id={self._id}, nombre='{self._nombre}', "
                f"cantidad={self._cantidad}, precio={self._precio:.2f})")

    def __str__(self) -> str:
        return f"[{self._id}] {self._nombre} | cant: {self._cantidad} | $ {self._precio:.2f}"

    @staticmethod
    def _validar_id(v: int) -> int:
        if not isinstance(v, int):
            raise TypeError("El ID debe ser entero.")
        if v <= 0:
            raise ValueError("El ID debe ser > 0.")
        return v

    @staticmethod
    def _validar_nombre(v: str) -> str:
        if not isinstance(v, str):
            raise TypeError("El nombre debe ser texto.")
        nv = v.strip()
        if not nv:
            raise ValueError("El nombre no puede estar vacío.")
        return nv

    @staticmethod
    def _validar_cantidad(v: int) -> int:
        if not isinstance(v, int):
            raise TypeError("La cantidad debe ser entero.")
        if v < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return v

    @staticmethod
    def _validar_precio(v: float) -> float:
        try:
            fv = float(v)
        except (TypeError, ValueError):
            raise TypeError("El precio debe ser numérico.")
        if fv < 0:
            raise ValueError("El precio no puede ser negativo.")
        return fv
