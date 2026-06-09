#Precios
medicamentos = 28000
consulta = 18000
#Ingreso de datos
print("¡Hola! Bienvenido al programa para generar su bono medico.")
edad = int(input("Ingrese su edad: "))
plan = input(f"Ingrese su plan medico (A, B, C o D): ").upper()
#Ifs de descuento
if edad <= 30:
    if plan == "A":
        medicamentos = medicamentos * 0.78
        consulta = consulta * 0.88
        print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
    elif plan == "B":
        medicamentos = medicamentos * 0.78
        consulta = consulta * 0.88
        print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
    elif plan == "C":
        medicamentos = medicamentos * 0.85
        print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
    elif plan == "D":
        medicamentos = medicamentos * 0.85
        print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
elif edad >= 31 and edad <= 60:
    if plan == "A":
        medicamentos = medicamentos * 0.85
        if edad >= 55:
            consulta = consulta * 0.94
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
        else:
            consulta = consulta * 0.88
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
    elif plan == "B":
        medicamentos = medicamentos * 0.85
        if edad >= 55:
            consulta = consulta * 0.94
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")       
        else:
            consulta = consulta * 0.88
            print(f"El valor de los medicamentos es: {int(medicamentos) }\nEl valor de la consulta es: {int(consulta)}")
    elif plan == "C":
        medicamentos = medicamentos * 0.9
        if edad >= 55:
            consulta = consulta * 1.06
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
        else:
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
    elif plan == "D":
        medicamentos = medicamentos * 0.9
        if edad >= 55:
            consulta = consulta * 1.06
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
        else:
            print(f"El valor de los medicamentos es: {int(medicamentos)}\nEl valor de la consulta es: {int(consulta)}")
elif edad > 60:
    if plan == "A":
        consulta = consulta * 0.94
        print(f"El valor de la consulta es: {int(consulta)}")
    elif plan == "B":
        consulta = consulta * 0.94
        print(f"El valor de la consulta es: {int(consulta)}")
    elif plan == "C":
        consulta = consulta * 1.06
        print(f"El valor de la consulta es: {int(consulta)}")
    elif plan == "D":
        consulta = consulta * 1.06
        print(f"El valor de la consulta es: {int(consulta)}")
