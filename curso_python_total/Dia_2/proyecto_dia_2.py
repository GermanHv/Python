# Proyecto día 2
# Programa que pregunte al usuario su nombre y cuántas ventas ha hecho
# de las ventas calcular el monto que le corresponde a su comisión %13
nombre = input("Ingresa tu nombre: ")
ventas = float(input("Ingresa tu ventas del mes: "))
monto = round(ventas * .13, 2)

print(f"\nBuen día {nombre}, tu monto a recibir este mes es de: ${monto}")

