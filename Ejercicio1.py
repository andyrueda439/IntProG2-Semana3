## Leer x cantidad de producto comprado a x precio,
#aplica el iva del 15%
# un descuento del 10
#mostrar el Total antes del IVA
#Monto del Iva
#Monto de descuento
#Total a pagar
"""Se debe leer el nombre del cliente, nombre del producto y mostrar 
una factura"""
print("="*20)
print("Sistema de Facturacion")
print("="*20)
print("Ingresa los siguintes datos")
cliente = input("Nombre del cliente: ")
producto = input("Nombre del producto: ")
precio = float(input("Precio del producto"))
cantidad = float(input("Cantidad del producto"))

total = precio * cantidad
iva = total * 0.15
descuento = total * 0.1
monto = total + iva  - descuento

import os
press_key = input("Presiona una tecla para contnuar....")
os.system("cls || clear")
print("+"*30)
print("Factura")
print("+"*30)
print(f"Cliente: {cliente}")
print(f"Productos \t Cantidad \t Precio \t Total")
print(f"{producto} \t {cantidad} \t {precio} \t {total}")
print(f"IVA: {iva}")
print(f"Desc: {descuento}")
print(f"Monto: {monto}")