#Ingreso de nombre
usuario = input("Ingrese su nombre de usuario: ")
#Validación del nombre de usuario
#Usamos len para verificar la longitud del nombre de usuario, isalpha para verificar que el primer 
# carácter sea una letra y isalnum para verificar que el nombre de usuario contenga solo caracteres alfanuméricos.
if len(usuario)>5 and len(usuario)<15 and usuario[0].isalpha() and usuario.isalnum():
    print("Usuario válido")
elif len(usuario)<=5 or len(usuario)>=15:
    print("El nombre de usuario debe tener entre 6 y 14 caracteres")
else:
    print("El nombre de usuario debe comenzar con una letra y contener solo caracteres alfanuméricos")
