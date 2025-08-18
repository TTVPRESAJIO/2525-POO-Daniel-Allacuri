# producto.py
from __future__ import annotations

class Producto:
    def __init__(self, id: int, nombre: str, cantidad: int, precio: float) -> None:
        # Constructor: valida y deja el objeto en estado consistente
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
    def id(self, _nuevo_id: int) -> None:
        raise AttributeError("El ID de un producto no puede cambiar una vez creado.")

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        self._nombre = self._validar_nombre(nuevo_nombre)

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int) -> None:
        self._cantidad = self._validar_cantidad(nueva_cantidad)

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        self._precio = self._validar_precio(nuevo_precio)

    def __repr__(self) -> str:
        return (f"Producto(id={self._id}, nombre='{self._nombre}', "
                f"cantidad={self._cantidad}, precio={self._precio:.2f})")

    def __str__(self) -> str:
        return f"[{self._id}] {self._nombre} | cant: {self._cantidad} | $ {self._precio:.2f}"

    @staticmethod
    def _validar_id(valor: int) -> int:
        if not isinstance(valor, int):
            raise TypeError("El ID debe ser un entero.")
        if valor <= 0:
            raise ValueError("El ID debe ser un entero positivo.")
        return valor

    @staticmethod
    def _validar_nombre(valor: str) -> str:
        if not isinstance(valor, str):
            raise TypeError("El nombre debe ser una cadena.")
        nombre = valor.strip()
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        return nombre

    @staticmethod
    def _validar_cantidad(valor: int) -> int:
        if not isinstance(valor, int):
            raise TypeError("La cantidad debe ser un entero.")
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        return valor

    @staticmethod
    def _validar_precio(valor: float) -> float:
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise TypeError("El precio debe ser numérico.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        return precio
