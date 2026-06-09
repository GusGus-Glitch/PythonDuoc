telefono = input("Ingrese su número de teléfono: ").strip()
telefono = telefono.replace(" ", "").replace("+", "").replace("-", "").replace("(", "").replace(")", "")
if telefono[0:2] == "56":
    telefono = telefono[2:]
if len(telefono) != 9:
    print(f"Cantidad de numeros invalido. Se necesitan 9 numeros")
else:
    parte1 = telefono[0]
    parte2 = telefono[1:5]
    parte3 = telefono[5:9]
    
    print(f"Su numero es +56 {parte1} {parte2} {parte3}")