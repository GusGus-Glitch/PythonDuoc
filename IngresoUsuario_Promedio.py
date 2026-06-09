#Ingreso de edad
edad = int(input("Ingrese su edad: "))
#Condicional para verificar que sea mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
#Ingreso de usuario
user = input("Ingrese su nombre de usuario: ")
match user:
#Opcion de pedro
    case "pedro":
        password =  input("Ingrese su contraseña: ")
        if password == "1234":  
            print("Bienvenido Pedro")
            print("Ingrese sus notas al sistema.")
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            promedio = (nota1 + nota2 + nota3) / 3
            if promedio >= 4.0:
             print(f"Su promedio es: {promedio:.2f}")
             print("Aprobado")
            else: 
             print(f"Su promedio es: {promedio:.2f}")            
             print("Reprobado")

        else:            
            print("Contraseña incorrecta")
#Opcion de angel
    case "angel":
        password = input("Ingrese su contraseña: ")
        if password == "a4s1":
            print("Bienvenido Angel")
            print("Ingrese sus notas al sistema.")
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            promedio = (nota1 + nota2 + nota3) / 3
            if promedio >= 4.0:
             print(f"Su promedio es: {promedio:.2f}")
             print("Aprobado")
            else: 
             print(f"Su promedio es: {promedio:.2f}")            
             print("Reprobado")

        else:            
            print("Contraseña incorrecta")