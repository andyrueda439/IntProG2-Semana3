def calcular_tiempo_total(duracion_pelicula, comerciales_previos, pausas, duracion_pausa):
    total_comerciales_pausas = pausas * duracion_pausa
    duracion_total = duracion_pelicula + comerciales_previos + total_comerciales_pausas

    return duracion_total, total_comerciales_pausas

# Ingresar datos
peliculas_min = float(input("Ingrese la duracion de la pelicula en minutos: "))
comerciales_previos = float(input("Ingrese la duracion de los comerciales previos en minutos: "))
pausas = int(input("Ingrese la cantidad de pausas comerciales durante la pelicula: "))
duracion_pausa = float(input("Ingrese la duracion de la pausa comercial en minutos: "))

# Calcular tiempos
duracion_total, total_comerciales_pausas = calcular_tiempo_total(peliculas_min, comerciales_previos, pausas, duracion_pausa)

# Mostrar resultados
print(f"Duracion original de la pelicula: {peliculas_min:.2f} minutos")
print(f"Duracion total de los comerciales (previos + durante la pelicula): {comerciales_previos + total_comerciales_pausas:.2f} minutos")
print(f"Tiempo total de la proyeccion: {duracion_total:.2f} minutos")