import math

def calcular_cilindro(radio, altura):
    area_base = math.pi * radio ** 2
    volumen = area_base * altura
    area_lateral = 2 * math.pi * radio * altura
    area_total = area_lateral + 2 * area_base

    return volumen, area_total

# Ingresar datos
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular volumen y area superficial
volumen, area_superficial = calcular_cilindro(radio, altura)

# Motrar resultados
print(f"Radio ingresado: {radio:.2f}")
print(f"Altura ingresada: {altura:.2f}")
print(f"Volumen del cilindro: {volumen:.2f}")
print(f"Area superficial del cilindro: {area_superficial:.2f}")