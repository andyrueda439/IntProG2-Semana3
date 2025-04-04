def calcular_area_perimetro():
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))

    area = base * altura
    perimetro = 2 * (base + altura)

    print(f"El area del rectangulo es: {area}")
    print(f"El perimetro del rectangulo es: {perimetro}")