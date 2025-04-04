def calcular_salario_neto():
    salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
    impuesto_renta = salario_bruto * 0.10
    seguro_social = salario_bruto * 0.05
    fondo_pensiones = salario_bruto * 0.02

    total_descuentos = impuesto_renta + seguro_social + fondo_pensiones
    salario_neto = salario_bruto - total_descuentos

    print(f"Salario bruto: {salario_bruto}")
    print(f"Total descuentos: {total_descuentos}")
    print(f"Salario neto: {salario_neto}")