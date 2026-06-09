#Definimos las variables en true para iniciar los bucles.
homa = True
noma = True
oma = True
#Definimos las variables para los contadores.
cant_prioritarios = 0
cant_general = 0
cant_pacientes = 0
#Iniciamos el programa
print ("Bienvenido al programa de ingreso de pacientes")
#Iniciamos un bucle para verificar que los datos sean ingresados como se debe
while oma == True:
    cantidad = int(input("Ingrese la cantidad de pacientes a registrar: "))
    if cantidad <= 0:
        print("La cantidad debe ser un número positivo. Intente nuevamente.")
    else:
        cant_pacientes = cantidad
        oma = False
#Creamos un ciclo for para que se adapte a la cantidad de pacientes ingresados
for i in range(cant_pacientes):
    #Lo màs importante fue volver a poner homa y noma en true al inicio del bucle para que se vuelva a repetir el proceso de verificación de datos para cada paciente.
    homa = True
    noma = True
    print (f"Paciente nº{i+1}:")
    #Bucle para verificar longitud y caracteres en el codigo
    while homa == True:
        codigo = input("Ingrese el codigo de atencion del paciente: ")
        if len(codigo) < 6 or (codigo.count(" ") != 0):
            print("El codigo debe tener minimo 6 caracteres y no contener espacios. Intente nuevamente.")
        else:
            homa = False
    #Bucle para verificar que la edad sea un numero entero y no negativa
    while noma == True:
        try:
            edad = int(input("Ingrese la edad del paciente: "))
        except ValueError:
            print("La edad debe ser un número entero. Intente nuevamente.")
            continue
        if edad < 0:
            print("La edad no puede ser negativa. Intente nuevamente.")
        else:
            if edad >= 65:
                print("El paciente es prioritario.")
                cant_prioritarios += 1
            else:
                print("El paciente es general.")
                cant_general += 1
            noma = False
#Output final
print (f"Se registraron {cant_prioritarios} pacientes prioritarios y {cant_general} pacientes generales.")