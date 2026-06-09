#Precios
plan = 80000 #plan dental
radiografia = 12000 #radiografia dental
#Ingreso de datos
edad = int(input("Ingrese la edad del paciente: "))
#En el ejemplo se nos muestra que es del quintil 1 al 5
quintil = int(input("Ingrese el quintil socioeconómico del paciente (1-5): "))
#Cálculo del descuento
if edad <= 25:
    if quintil == 1:
        plan = plan * 0.82
        radiografia = radiografia * 0.9
    elif quintil == 2:
        plan = plan * 0.82
        radiografia = radiografia * 0.9
    elif quintil == 3:
        plan = plan * 0.88
        radiografia = radiografia * 0.9
    elif quintil == 4:
        plan = plan * 0.88
    elif quintil == 5:
        plan = plan
    else:
        print("Quintil no válido. Ingrese un número del 1 al 5.")
elif edad > 26 and edad <=45:
    if quintil == 1:
        plan = plan * 0.88
        if edad >= 40:
            radiografia = radiografia * 0.85
        else:
            radiografia = radiografia * 0.9
    elif quintil == 2:
        plan = plan * 0.88
        if edad >= 40:
            radiografia = radiografia * 0.85
        else:
            radiografia = radiografia * 0.9
    elif quintil == 3:
        plan = plan * 0.92
        if edad >= 40:
            radiografia = radiografia * 0.85

        else:
            radiografia = radiografia * 0.9
    elif quintil == 4:
        plan = plan * 0.92
        if edad >= 40:
            radiografia = radiografia
        else:
            radiografia = radiografia
    elif quintil == 5:
        plan = plan
        if edad >= 40:
            radiografia = radiografia
        else:
            radiografia = radiografia
    else:
        print("Quintil no válido. Ingrese un número del 1 al 5.")
elif edad > 45:
    if quintil == 1:
        radiografia = radiografia * 0.85
    elif quintil == 2:
        radiografia = radiografia * 0.85
    elif quintil == 3:
        radiografia = radiografia * 0.85
    elif quintil == 4:
        radiografia = radiografia
    elif quintil == 5:
        radiografia = radiografia
    else:
        print("Quintil no válido. Ingrese un número del 1 al 5.")


#Resultados
if quintil == 1 or quintil == 2 or quintil == 3 or quintil == 4 or quintil == 5:
    print(f"El valor del plan dental es: {int(plan)}\nEl valor de la radiografia dental es: {int(radiografia)}")
else:
    print("Adios, que tenga un buen día.")