def calcular_tiempo_viaje():
    tramo1 = float(input("Ingrese la duracion del primer tramo del vuelo: "))
    escala1 = float(input("Ingrese la duracion de la primera escala: "))
    tramo2 = float(input("Ingrese la duracion del segundo plano del vuelo: "))
    escala2 = float(input("Ingrese la duracion de la segunda escala: "))
    tramo3 = float(input("Ingrese la duracion del tercer tramo del vuelo: "))

    tiempo_total = tramo1 + escala1 + tramo2 + escala2 + tramo3

    print(f"El tiempo total del viaje es: {tiempo_total} horas")