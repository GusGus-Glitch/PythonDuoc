#Explicamos lo que hay que ingresar y guardamos el valor ingresado en una variable
print(f"A continuacion debe ingresar el nombre de su variable, pero debe tener en consideracion que \nel nombre de la variable no puede comenzar con un numero, no puede llevar espacios ni caracteres \nespeciales a excepcion del guion bajo (_) y no puede ser una palabra reservada del lenguaje python.")
variable = input("Ingrese su nombre de variable: ")
match variable:
    case variable if variable[0] ==r
        print("El nombre de la variable no puede comenzar con un numero.")
    case variable if ' ' in variable:
        print("El nombre de la variable no puede llevar espacios.")
    case variable if not variable.isidentifier():
        print("El nombre de la variable contiene caracteres especiales.")
    case _:
        print("El nombre de la variable es valido.")
