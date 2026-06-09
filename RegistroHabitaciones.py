oma = True
homa = True
hopa = True
hab_ejecutiva = 0
hab_estandar = 0
print ("Bienvenido al sistema de registro de habitaciones del Hotel Corporativo Internacional.")
while oma:
    try:
        cantidad = int(input("Ingrese la cantidad de habitaciones a registrar: "))
        if cantidad < 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            oma = False
    except ValueError:
        print("¡Dato inválido! Ingresa un valor numérico para continuar el registro")
for i in range(cantidad):
    homa = True
    while homa == True:
        try:
            numero = input(f"Ingrese el numero de la habitación nº {i+1} (No debe contener espacios): ")
            if len(numero) < 6 or " " in numero:
                print("Numero invalido. El numero debe tener al menos 6 caracteres y no llevar espacios.")
            else:
                homa = False

        except ValueError:
            print("¡Dato inválido! Ingresa un valor de texto para el numero de la habitación.")
    hopa = True
    while hopa == True:
        try:
            tarifa = int(input(f"Ingrese la tarifa nocturna de la habitación nº {i+1}: "))
            if tarifa < 0:
                print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")
            else:
                if tarifa >= 90000:
                    print(f"La habitación {numero} es una habitación ejecutiva.")
                    hab_ejecutiva += 1
                    hopa = False
                else:
                    print(f"La habitación {numero} es una habitación estándar.")
                    hab_estandar += 1
                    hopa = False
        except ValueError:
            print("¡Error tarifario! Ingresa un número entero positivo para la tarifa nocturna.")

print(f"¡El hotel cuenta con {hab_ejecutiva} habitaciones ejecutivas y {hab_estandar} habitaciones estandar!¡Check-in disponible!")