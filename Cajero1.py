saldo = 10000
while True:
    print("Bienvenido al banco, seleccione una opcion:\n 1. Consultar saldo\n 2. Retirar\n 3. Salir")
    opcion = input("Ingrese su opcion: ")
    if opcion == "1":
        print(f"Su saldo actual es: {saldo}")
    elif opcion == "2":
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= monto
            print(f"Retiro exitoso. Su nuevo saldo es: {saldo}")
    elif opcion == "3":
        print("Gracias por usar nuestros servicios. ¡Hasta luego!")
        break
    else:
        print("Opcion no valida, por favor intente de nuevo.")
