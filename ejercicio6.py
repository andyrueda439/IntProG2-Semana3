def calcular_imc():
    peso = float(input("Ingrese el peso en kilogramos : "))
    altura = float(input("Ingrese la altura en metros: "))

    imc = peso / (altura ** 2)
    imc = round(imc, 2)

    print(f"Peso ingresado: {peso} kg")
    print(f"Altura ingresada: {altura} m")
    print(f"IMC calculado: {imc}")

    if imc < 18.5:
        print("Clasificacion: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Clasificacion: Peso normal")
    elif 25 <= imc < 29.9:
        print("Clasificacion: Sobrepeso")
    else:
        print("Clasificacion: Obesidad")