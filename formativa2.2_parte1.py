nombrecompleto = input("Ingrese su nombre completo: ")
nombrecompleto.split()
if len(nombrecompleto.split()) < 2:
   print ("Debe ingresar al menos un nombre y un apellido.")
elif len(nombrecompleto.split()) > 2:
    print(f"Su nombre es: {nombrecompleto.split()[0].upper()} {nombrecompleto.split()[-1].lower()} {nombrecompleto.upper().split()[1][0]}")
elif len(nombrecompleto.split()) == 2:
    print(f"Su nombre es: {nombrecompleto.split()[0].upper()} {nombrecompleto.split()[-1].lower()}")