#Definimos la variable para el bucle del menu
condi = True
#Definimos las variables para los contadores
num_movimientos = 0
cant_disponibles = 20
cant_prestadas = 0
#Iniciamos el programa
print ("Bienvenido al programa de prestamo de bicicletas.")
#Iniciamos el bucle del menu, que solo puede pararse con la opcion salir
while condi == True:
    print("Menu de opciones:\n1. Cantidad de bicicletas disponibles\n2. Prestamo de bicicletas\n3. Devolucion de bicicletas\n4. Historial de prestamos\n5. Salir")
    #Agregamos un try except para verificar que la opcion ingresada sea un numero entero y no una letra o simbolo, y tambien para verificar que la opcion este dentro del rango de opciones disponibles.
    try:
        opcion = int(input("Seleccione una opción: "))
        #Mostramos la cantidad de bicicletas disponibles, y luego volvemos al menu
        if opcion == 1:
            print (f"Actualmente hay {cant_disponibles} bicicletas disponibles.")
            continue
        #Agregamos las condicionales base,y ademas le añadimos que no puedan prestarse màs bicicletas de las que hay disponibles.
        elif opcion == 2:
            try:
                cantidad_prestamo = int(input("Ingrese la cantidad de bicicletas a prestar: "))
                if cantidad_prestamo <= 0:
                    print("La cantidad debe ser un numero positivo. Intente nuevamente.")
                    continue
                elif cantidad_prestamo > cant_disponibles:
                    print(f"No hay suficientes bicicletas disponibles. Solo hay {cant_disponibles} bicicletas disponibles. Intente nuevamente.")
                    continue
                #Aqui los contadores hacen su magia, restamos las prestadas de las disponibles, sumamos las prestadas al contador de prestadas, y sumamos una al contador de movimientos.
                else:
                    cant_disponibles -= cantidad_prestamo
                    cant_prestadas += cantidad_prestamo
                    num_movimientos += 1
                    print(f"Se han prestado {cantidad_prestamo} bicicletas. Quedan {cant_disponibles} bicicletas disponibles.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue
        #Agregamos las condicionales base, y ademas le añadimos que no puedan devolverse màs bicicletas de las que hay en la capacidad maxima, que son 20.
        elif opcion == 3:
            try:
                cantidad_devolucion = int(input("Ingrese la cantidad de bicicletas a devolver: "))
                if cantidad_devolucion <= 0:
                    print("La cantidad debe ser un numero positivo. Intente nuevamente.")
                    continue
                elif cantidad_devolucion + cant_disponibles > 20:
                    print(f"No se pueden devolver más bicicletas de las que hay en la capacidad maxima, que son 20. Intente nuevamente.")
                    continue
                #Al verificar que se cumplan las condiciones, sumamos las bicicletas devueltas a las disponibles, restamos las bicicletas devueltas de las prestadas, y sumamos una al contador de movimientos.
                else:
                    cant_disponibles += cantidad_devolucion
                    cant_prestadas -= cantidad_devolucion
                    print(f"Se han devuelto {cantidad_devolucion} bicicletas. Ahora hay {cant_disponibles} bicicletas disponibles.")
                    num_movimientos += 1
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue
        #No hay mucha ciencia, solo mostramos con los contadores la cantidad de prestadas, y el contador de movimientos, que se incrementa con prestamos como devoluciones
        elif opcion == 4:
            print(f"Actualmente hay prestadas {cant_prestadas} bicicletas.\nNumero total de movimientos(Prestamos y devoluciones): {num_movimientos}")
        #Al seleccionar esta opcion, nos despedimos, y cambiamos el con a false para salir del bucle del menu, que era la condicional para que el programa siga funcionando.
        elif opcion == 5:
            print("Gracias por usar el programa de prestamo de bicicletas. ¡Hasta luego!")
            condi = False
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 5.")
    #Este es el except que va de la mano con el try que va al inicio del bucle del menu, para verificar que la opcion ingresada sea un numero entero y no una letra o simbolo, y tambien para verificar que la opcion este dentro del rango de opciones disponibles.
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")
