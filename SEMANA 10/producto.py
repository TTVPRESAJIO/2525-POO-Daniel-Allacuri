# producto.py
from __future__ import annotations

class Producto:
    def __init__(self, id: int, nombre: str, cantidad: int, precio: float) -> None:
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    @property
    def id(self): return self._id
    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, nuevo): self._nombre = nuevo.strip()

    @property
    def cantidad(self): return self._cantidad
    @cantidad.setter
    def cantidad(self, nueva): self._cantidad = nueva

    @property
    def precio(self): return self._precio
    @precio.setter
    def precio(self, nuevo): self._precio = nuevo

    def __str__(self):
        return f"[{self._id}] {self._nombre} | cant: {self._cantidad} | ${self._precio:.2f}"

    # Almacena el archivo
    def to_linea(self) -> str:
        return f"{self._id};{self._nombre};{self._cantidad};{self._precio}"

    @staticmethod
    def from_linea(linea: str) -> Producto:
        partes = linea.strip().split(";")
        return Producto(int(partes[0]), partes[1], int(partes[2]), float(partes[3]))
