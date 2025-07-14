# CREO LA CLASE QUE VOY A USAR
class BotellaDeAgua:
    def __init__(self, marca, capacidad_ml):
        self.marca = marca              # ESTOS SON LOS ATRIBUTOS QUE VAN A TENER MI CLASE
        self.capacidad = capacidad_ml
        print(f"Botella de '{self.marca}' de {self.capacidad}ml creada y lista para usar.")

    def beber(self, cantidad):
        # METODO PARA SIMULAR QUE SE BEBE DE LA BOTELLA
        if cantidad <= self.capacidad:
            self.capacidad -= cantidad
            print(f"Bebiste {cantidad}ml de agua. Quedan {self.capacidad}ml.")
        else:
            print("No hay suficiente agua para beber esa cantidad.")

    def __del__(self):
       # ES UN DESTRUCTOR QUE SE EJECUTA AL ELIMINAR EL OBJETO, IDEAL PARA FINALIZAR EL PROGRAMA O LIBERAR RECURSOS
        print(f"La botella de '{self.marca}' ha sido reciclada. ¡Gracias por cuidar el planeta!")

# AHROA VAMOS A EJECUTAR EL PROGRAMA

print("Inicio del programa...")

# CREAR UNA BOTELLA
botella = BotellaDeAgua("Cielo", 500)

# USAR LA BOTELLA
botella.beber(200)
botella.beber(100)

# ELIMINAR LA REFERENCIA A LA BOTELLA PARA ACTIVAR EL DESTRUCTOR
del botella

print("Fin del programa.")