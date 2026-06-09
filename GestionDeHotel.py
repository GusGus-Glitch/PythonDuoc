#Definimos la variable para el bucle del menu
condi = True
#Definimos las variables para los contadores
num_movimientos = 0
cant_disponibles = 50
cant_canceladas = 0
#Iniciamos el programa
print ("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!")
#Iniciamos el bucle del menu, que solo puede pararse con la opcion salir
while condi == True:
    print("Menu de opciones:\n1. Habitaciones disponibles\n2. Realizar check-in\n3. Realizar check-out\n4. Historial de ocupaciones\n5. Salir")
    #Agregamos un try except para verificar que la opcion ingresada sea un numero entero y no una letra o simbolo, y tambien para verificar que la opcion este dentro del rango de opciones disponibles.
    try:
        opcion = int(input("Seleccione una opción: "))
        #Mostramos la cantidad de habitaciones disponibles, y luego volvemos al menu
        if opcion == 1:
            print (f"Actualmente hay {cant_disponibles} habitaciones disponibles.")
            continue
        #Agregamos las condicionales base,y ademas le añadimos que no puedan prestarse màs habitaciones de las que hay disponibles.
        elif opcion == 2:
            try:
                cantidad_prestamo = int(input("Ingrese la cantidad de habitaciones a reservar: "))
                if cantidad_prestamo <= 0:
                    print("La cantidad debe ser un numero positivo. Intente nuevamente.")
                    continue
                elif cantidad_prestamo > cant_disponibles:
                    print(f"No hay suficientes habitaciones disponibles. Solo hay {cant_disponibles} habitaciones disponibles. Intente nuevamente.")
                    continue
                #Aqui los contadores hacen su magia, restamos las prestadas de las disponibles, sumamos las prestadas al contador de prestadas.
                else:
                    cant_disponibles -= cantidad_prestamo
                    cant_canceladas += cantidad_prestamo
                    print(f"Se han reservado {cantidad_prestamo} habitaciones. Quedan {cant_disponibles} habitaciones disponibles.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue
        #Agregamos las condicionales base, y ademas le añadimos que no puedan devolverse màs habitaciones de las que hay en la capacidad maxima, que son 20.
        elif opcion == 3:
            try:
                cantidad_devolucion = int(input("Ingrese la cantidad de habitaciones a cancelar: "))
                if cantidad_devolucion <= 0:
                    print("La cantidad debe ser un numero positivo. Intente nuevamente.")
                    continue
                elif cantidad_devolucion + cant_disponibles > 50:
                    print(f"No se pueden devolver más habitaciones de las que hay en la capacidad maxima, que son 50. Intente nuevamente.")
                    continue
                #Al verificar que se cumplan las condiciones, sumamos las habitaciones devueltas a las disponibles, restamos las habitaciones devueltas de las prestadas, y sumamos una al contador de movimientos.
                else:
                    cant_disponibles += cantidad_devolucion
                    cant_canceladas -= cantidad_devolucion
                    print(f"Se han cancelado {cantidad_devolucion} habitaciones. Ahora hay {cant_disponibles} habitaciones disponibles.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número entero.")
                continue
        #No hay mucha ciencia, solo mostramos con los contadores la cantidad de prestadas, y el contador de movimientos, que se incrementa con prestamos como devoluciones
        elif opcion == 4:
            print(f"Actualmente hay canceladas {cant_canceladas} habitaciones.")
        #Al seleccionar esta opcion, nos despedimos, y cambiamos el con a false para salir del bucle del menu, que era la condicional para que el programa siga funcionando.
        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            condi = False
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 5.")
    #Este es el except que va de la mano con el try que va al inicio del bucle del menu, para verificar que la opcion ingresada sea un numero entero y no una letra o simbolo, y tambien para verificar que la opcion este dentro del rango de opciones disponibles.
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")
