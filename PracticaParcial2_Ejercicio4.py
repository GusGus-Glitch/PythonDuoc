correo = input("Ingrese su correo: ").strip()

if correo.count("@") == 1 and not correo.startswith("@") and (correo.endswith(".org") or correo.endswith(".com")):
    print("Correo válido")
elif correo.count != 1:
    print("Correo no válido: debe contener exactamente un '@'")
else:
    print("El correo debe terminar en '.org' o '.com' y no empezar con '@'")