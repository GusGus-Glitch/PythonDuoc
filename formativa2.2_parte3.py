correo = input("Ingrese su correo electrónico: ")
usuario = correo.split("@")[0]
dominio = correo.split("@")[-1]
extension = correo.split(".")[-1]
if correo.count("@") != 1:
    print("El correo electrónico no es válido. Debe contener solo un '@'")

else:
        if correo.count(".") == 0:
            print("El correo electrónico no es válido. Debe contener al menos un '.'")
        else:
            if correo[0][0] == ".":
                print("El correo electrónico no es válido. No puede comenzar con un '.'")
            else: 
                if extension != "com":
                    print("El correo electrónico no es válido. La extensión debe ser '.com'")
                else:
                    print(f"El nombre de usuario es: {usuario}, el dominio es: {dominio} y la extensión es: {extension}")