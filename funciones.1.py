def resta(a, b):
    return a - b
resta(30, 10)

def resta(a, b):
    return a - b
resta(b=30, a=10)

def funcion():
    return "Bienvenidos a python"
frase = funcion()
print(frase)

def resta(a=None, b=None):
    if a is None or b is None:
        return "Error: Se requieren ambos parámetros"
    return a - b

def calculo(precio, descuento):
    return precio - (precio * descuento / 100)
datos = [10000, 10]
print ("El monto final a pagar es:", calculo(*datos))

def saludo(nombre, mensaje='Python'):
    print(mensaje, nombre)
saludo(mensaje="Buen día", nombre="Pedro")