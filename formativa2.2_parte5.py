contra = input("Ingrese la contraseña: ")
fortaleza = 0
if len(contra) <= 8:
    fortaleza += 1
else: fortaleza +=0
if contra != contra.lower():
    fortaleza += 1
else: fortaleza +=0
if contra != contra.upper():
    fortaleza += 1
else: fortaleza +=0
if any(caracter.isdigit() for caracter in contra):
    fortaleza += 1
else: fortaleza +=0
if fortaleza == 1:
    print("Contraseña muy débil")
elif fortaleza == 2:
    print("Contraseña débil")
elif fortaleza == 3:
    print("Contraseña media")
elif fortaleza == 4:
    print("Contraseña fuerte")
