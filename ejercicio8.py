def convertir_monedas(cantidad_dolares, tasa_euro, tasa_libra, tasa_yen):
    cantidad_euros = cantidad_dolares * tasa_euro
    cantidad_libras = cantidad_dolares * tasa_libra
    cantidad_yenes = cantidad_dolares * tasa_yen

    return cantidad_euros, cantidad_libras, cantidad_yenes

# Ingresar la cantidad en dolares
cantidad_dolares = float(input("Ingrese la cantidad en dolares: "))

# Definir las tasas de cambio
tasa_euro = float(input("Ingrese la tasa de cambio de dolares a euros: "))
tasa_libra = float(input("Ingrese la tasa de cambio de dolares a libras: "))
tasa_yen = float(input("Ingrese la tasa de cambio de dolares a yenes: "))

# Realizar la conversion
euros, libras, yenes = convertir_monedas(cantidad_dolares, tasa_euro, tasa_libra, tasa_yen)

# Mostrar los resultados
print(f"Cantidad en dolares: {cantidad_dolares:.2f}")
print(f"Cantidad en euros: {euros:.2f}")
print(f"Cantidad en libras: {libras:.2f}")
print(f"Cantidad en yenes: {yenes:.2f}")