condi = True
cantidad_ocupada = 0
cant_disponibles = 60
total_ocupadas = 0
print ("¡Bienvenido al sistema de almacenamiento del almacen industrial!")
while condi == True:
    print("Menu de opciones:\n1. Espacios disponibles\n2. Ocupar espacio\n3. Liberar espacio\n4. Historial de ocupaciones\n5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            print (f"Actualmente hay {cant_disponibles} espacios disponibles.")
            continue
        elif opcion == 2:
            if cant_disponibles == 0:
                print("No hay espacios disponibles para ocupar. Por favor libere algunos espacios antes de intentar ocupar más.")
                continue
            else:
                oma = True
                while oma == True:
                    try:
                        cantidad_ocupada = int(input("Ingrese la cantidad de espacios a reservar: "))
                    except ValueError:
                        print("Entrada no válida. Por favor ingrese un número entero.")
                        continue
                    if cantidad_ocupada <= 0:
                        print("La cantidad debe ser un numero positivo. Intente nuevamente.")
                        continue
                    elif cantidad_ocupada > cant_disponibles:
                        print(f"No hay suficientes espacios disponibles. Solo hay {cant_disponibles} espacios disponibles. Intente nuevamente.")
                        continue
                    else:
                        cant_disponibles -= cantidad_ocupada
                        total_ocupadas += cantidad_ocupada
                        print(f"Se han ocupado {cantidad_ocupada} espacios. Quedan {cant_disponibles} espacios disponibles.")
                        oma = False
        elif opcion == 3:
            if total_ocupadas == 0:
                print(f"No hay ningun espacio ocupado para liberar.")
            else:
                homa = True
                print (f"Actualmente hay ocupados {total_ocupadas} espacios.")
                while homa == True:
                    try:
                        cantidad_devolucion = int(input("Ingrese la cantidad de espacios a liberar: "))
                        if cantidad_devolucion <= 0:
                            print("La cantidad debe ser un numero positivo. Intente nuevamente.")
                            continue
                        elif cantidad_devolucion + cant_disponibles > 60:
                            print(f"No se pueden liberar más espacios de los que hay, que son 60. Intente nuevamente.")
                            continue
                        else:
                            cant_disponibles += cantidad_devolucion
                            total_ocupadas -= cantidad_devolucion
                            print(f"Se han liberado {cantidad_devolucion} espacios. Ahora hay {cant_disponibles} espacios disponibles.")
                            homa = False
                    except ValueError:
                        print("Entrada no válida. Por favor ingrese un número entero.")
                        continue
        elif opcion == 4:
            print(f"Actualmente hay ocupados {total_ocupadas} espacios.")
        elif opcion == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            condi = False
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 5.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")
