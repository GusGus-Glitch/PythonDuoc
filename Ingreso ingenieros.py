oma = True
homa = True
hopa = True
ing_senior = 0
ing_junior = 0
print ("Bienvenido al sistema de ingreso de ingenieros del instituto de ingeniería avanzada.")
while oma:
    try:
        cantidad = int(input("Ingrese la cantidad de ingenieros a ingresar: "))  
        if cantidad < 0:
            print("¡Dato inválido! Ingresa un entero positivo para continuar el registro")
        else:
            oma = False
    except ValueError:
        print("¡Dato inválido! Ingresa un valor numérico para continuar el registro")
for i in range(cantidad):
    homa = True
    while homa == True:
        try:
            nombre = input(f"Ingrese el nombre del ingeniero nº {i+1} (No debe contener espacios): ")
            if len(nombre) < 6 or " " in nombre:
                print("Nombre invalido. El nombre debe tener al menos 6 caracteres y no llevar espacios.")
            else:
                homa = False

        except ValueError:
            print("¡Dato inválido! Ingresa un valor de texto para el nombre del ingeniero.")
    hopa = True
    while hopa == True:
        try:
            nivel = int(input(f"Ingrese el nivel tecnico del ingeniero nº {i+1} (1-100): "))
            if nivel < 1 or nivel > 100:
                print("Nivel técnico inválido. Ingresa un valor entre 1 y 100.")
            else:
                if nivel >= 45:
                    print(f"El ingeniero {nombre} es un ingeniero senior.")
                    ing_senior += 1
                    hopa = False
                else:
                    print(f"El ingeniero {nombre} es un ingeniero junior.")
                    ing_junior += 1
                    hopa = False
        except ValueError:
            print("¡Dato inválido! Ingresa un valor numérico para el nivel técnico.")

print(f"¡El instituto cuenta con {ing_senior} Ingenieros Senior y {ing_junior} Ingenieros Junior!\n¡Registro completado satisfactoriamente!")