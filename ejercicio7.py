def calcular_precio_final():
    precio_original = float(input("Ingrese el precio original del producto: "))
    descuento = float(input("Ingrese el porcentaje del descuento"))

    monto_descuento = (precio_original * descuento) / 100
    precio_con_descuento = precio_original - monto_descuento

    iva = float(input("Ingrese el porcentaje en IVA: "))
    monto_iva = (precio_con_descuento * iva) / 100
    precio_final = precio_con_descuento + monto_iva

    print(f"Precio original: {precio_original}")
    print(f"Descuento aplicado: {monto_descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"IVA calculado: {monto_iva}")
    print(f"Precio final: {precio_final}")