nombre = input("Ingrese su nombre: ").strip()

if nombre == "":
    print("No se ha ingresado un nombre.")
elif nombre.islower() or nombre.isupper():
    nombre_formateado = nombre.title()
    print(f"Nombre formateado: {nombre_formateado}")
else:
    print(f"Nombre ingresado: {nombre}")