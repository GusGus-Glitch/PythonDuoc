#Ingresamos la contraseña del usuario
password = input("Ingrese su contraseña: ")
#Damos los condicionales para verificar que la contraseña cumpla los requisitos
#y verificamos su fortaleza
if len(password) >= 8 and not password.isalpha() and not password.isnumeric() and password.find  (" ") == -1:
    print("Contraseña fuerte")
elif len(password) < 8:
    print("Contraseña corta: debe tener al menos 8 caracteres")
else:
    print("La contraseña debe iniciar con una letra mayúscula, contener al menos un número y no contener espacios")