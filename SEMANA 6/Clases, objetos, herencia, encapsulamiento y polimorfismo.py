# sistema de gestión de empleados

#CLASE BASE: PERSONA

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


# Clase derivada: Empleado (hereda de Persona)
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto, salario):
        super().__init__(nombre, edad)  # Hereda nombre y edad de Persona
        self.puesto = puesto
        self.__salario = salario  # Atributo encapsulado (privado)

    # Método getter para acceder al salario (encapsulación)
    def obtener_salario(self):
        return self.__salario

    # Método setter para modificar el salario con control
    def establecer_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Error: El salario debe ser positivo.")

    # Polimorfismo (sobrescritura del método de la clase base)
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}, Salario: ${self.__salario}")


# Clase derivada adicional: Gerente
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, "Gerente", salario)
        self.departamento = departamento

    # Sobrescribe el método mostrar_informacion con información adicional
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}, "
              f"Departamento: {self.departamento}, Salario: ${self.obtener_salario()}")


# -------------------------------
# Uso del programa (instanciación)
# -------------------------------

# Crear un empleado
empleado1 = Empleado("Carlos", 30, "Desarrollador", 1200)
empleado1.mostrar_informacion()

# Modificar salario usando el setter
empleado1.establecer_salario(1500)
print("Salario actualizado:", empleado1.obtener_salario())

print()  # Separador

# Crear un gerente
gerente1 = Gerente("Lucía", 40, 2500, "Tecnología")
gerente1.mostrar_informacion()


