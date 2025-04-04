def convertir_segundos():
    segundos_totales = int(input("Ingrese la cantidad total de segundos: "))
    horas = segundos_totales // 3600
    segundos_restantes = segundos_totales % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    print(f"{horas} horas, {minutos} minutos y {segundos} segundos")