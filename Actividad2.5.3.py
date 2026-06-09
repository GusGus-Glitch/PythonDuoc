#Datos
deuda = 100000
saldo = 200000
while True:
    print("Bienvenido al programa de deudas y compras.\n1.Pago de tarjeta de credito\n2.Simulacion de compra\n3.Salir")
    try:
        opcion = int(input("Ingrese el número de la opción deseada: "))
        if opcion == 1:
            print(f"Su deuda actual es de: {deuda}")
            pago = int(input("Ingrese el monto a pagar: "))
            if pago > deuda:
                print("El pago no puede exceder la deuda actual.")
            elif pago < 0:
                print("El pago no puede ser negativo.")
            else:
                deuda -= pago
                print(f"Pago realizado. Deuda restante: {deuda}")

