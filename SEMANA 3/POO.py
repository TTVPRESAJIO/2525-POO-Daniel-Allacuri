# Información diaria del clima
class ClimaDia:
    def __init__(self, temperatura=0.0):
        self.__temperatura = temperatura  # Encapsulamiento

    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

# Clase derivada que maneja el clima semanal
class SemanaClimatica:
    def __init__(self):
        self.dias = []  # Lista de objetos ClimaDia

    def ingresar_temperaturas(self):
        print("Ingrese la temperatura de cada día de la semana:")
        for i in range(1, 8):
            temp = float(input(f"Día {i}: "))
            dia = ClimaDia()
            dia.set_temperatura(temp)
            self.dias.append(dia)

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)

    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f} °C")

# Clase alternativa para aplicar polimorfismo (opcional)
class SemanaCaliente(SemanaClimatica):
    def mostrar_resultado(self):
        promedio = self.calcular_promedio()
        print(f"\n¡Semana calurosa! El promedio fue: {promedio:.2f} °C")

# Programa principal
def main():
    semana = SemanaClimatica()
    semana.ingresar_temperaturas()
    semana.mostrar_resultado()

# Ejecutar el programa
main()
