#Codigo para calcular el area de un triangulo

# Lo primero es definir la funcion
def calcular_area_triangulo(base: float, altura: float) -> float:
    area = (base * altura)/2
    return area
print("calcular_area_triangulo")

#Vamos a pedir los datos del triangulo al usuario
base_input= input("Ingresa la base del triángulo (en cm): ")
altura_input= input("Ingresa la altura del triángulo (en cm): ")

base=float(base_input)
altura=float(altura_input)

area_resultado = calcular_area_triangulo(base, altura)
area_valida = area_resultado > 0

# De acuerdo a los datos datos la funcion trabaja y nos da el resultado
print("\nResultado:")
print("base:", base, "cm")
print("altura:", altura,"cm")
print("area del triangulo:", area_resultado, "cm^2")