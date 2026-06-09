nombre = input ("Ingrese su nombre completo: ")
nombre = nombre.replace(" ", "").lower()
if len(nombre) > 10:
    print("su nombre es demasiado largo")
    print(f"{nombre[:9]}")
else: 
    print(f"su nombre es: {nombre}")