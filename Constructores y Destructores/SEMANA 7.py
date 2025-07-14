# Clase que representa una botella de agua
class BotellaDeAgua:
    def __init__(self, marca, capacidad_ml):
        """
        Constructor (__init__):
        Se ejecuta automáticamente al crear un objeto de la clase.
        Sirve para establecer el estado inicial del objeto.
        """
        self.marca = marca              # Atributo: marca de la botella
        self.capacidad = capacidad_ml   # Atributo: capacidad en mililitros
        print(f"Botella de '{self.marca}' de {self.capacidad}ml creada y lista para usar.")

    def beber(self, cantidad):
        """
        Método para simular que se bebe agua de la botella.
        """
        if cantidad <= self.capacidad:
            self.capacidad -= cantidad
            print(f"Bebiste {cantidad}ml de agua. Quedan {self.capacidad}ml.")
        else:
            print("No hay suficiente agua para beber esa cantidad.")

    def __del__(self):
        """
        Destructor (__del__):
        Se ejecuta automáticamente cuando el objeto se va a eliminar.
        Ideal para liberar recursos o mostrar mensajes de cierre.
        """
        print(f"La botella de '{self.marca}' ha sido reciclada. ¡Gracias por cuidar el planeta!")

# --- Ejecución del programa ---

print("Inicio del programa...")

# Crear una botella
botella = BotellaDeAgua("Cielo", 500)

# Usar la botella
botella.beber(200)
botella.beber(100)

# Eliminar la referencia a la botella para activar el destructor
del botella

print("Fin del programa.")

