#Importamos randint para generar números aleatorios
from random import randint
print("Bienvenido al juego de adivinar el número aleatorio.")
print("Ingrese dos números enteros para definir el rango numérico.")
num1 = int(input("Ingrese el primer número (debe ser menor que el segundo): "))
num2 = int(input("Ingrese el segundo número (debe ser mayor que el primero): "))
#Validamos que el primer número sea menor que el segundo
if num1 >= num2:
    print("Error: El primer número debe ser menor que el segundo. Por favor, intente de nuevo.")
else:
#Generamos un número aleatorio entre num1 y num2
    numero_aleatorio = randint(num1, num2)
#Si el numero generado es impar, se debe transformar a par sumándole 1, siempre y cuando no se pase del rango definido por el usuario. Si se pasa del rango, se debe transformar a par restándole 1.
    if numero_aleatorio % 2 != 0:
        if numero_aleatorio + 1 <= num2:
            numero_aleatorio += 1
        else:
            numero_aleatorio -= 1
print("Ya se ha generado el numero aleatorio. ¡Intenta adivinarlo! \n Tienes 3 intentos.")
intento1 = int(input("Ingrese su primer intento: "))
if intento1 == numero_aleatorio:
    print("¡Felicidades! Has adivinado el número aleatorio.")
elif intento1 > numero_aleatorio:
    print("El número aleatorio es menor que el que ingresaste.")
elif intento1 < numero_aleatorio:
    print("El número aleatorio es mayor que el que ingresaste.")
#En este segundo intento, si falla se debe dar una pista, indicando si el numero aleatorio esta màs cerca del primer intento o del segundo.
intento2 = int(input("Ingrese su segundo intento: "))
if intento2 == numero_aleatorio:
    print("¡Felicidades! Has adivinado el número aleatorio.")
elif intento2 > numero_aleatorio:
    print("El número aleatorio es menor que el que ingresaste.")
#Calculamos la distancia entre el numero aleatorio y los intentos
    distancia_intento1 = (numero_aleatorio - intento1)
    if distancia_intento1 < 0:
        distancia_intento1 = distancia_intento1 * -1
    distancia_intento2 = (numero_aleatorio - intento2)
    if distancia_intento2 < 0:
        distancia_intento2 = distancia_intento2 * -1
    if distancia_intento1 < distancia_intento2:
        print(f"Estás más cerca del {intento1} que de {intento2}.")
    else:
        print(f"Estás más cerca del {intento2} que de {intento1}.")

elif intento2 < numero_aleatorio:
    print("El número aleatorio es mayor que el que ingresaste.")
#Calculamos la distancia entre el numero aleatorio y los intentos
    distancia_intento1 = (numero_aleatorio - intento1)
    if distancia_intento1 < 0:
        distancia_intento1 = distancia_intento1 * -1
    distancia_intento2 = (numero_aleatorio - intento2)
    if distancia_intento2 < 0:
        distancia_intento2 = distancia_intento2 * -1
    if distancia_intento1 < distancia_intento2:
        print(f"Estás más cerca del {intento1} que de {intento2}.")
    else:
        print(f"Estás más cerca del {intento2} que de {intento1}.")
#En este tercer intento, si falla se muestra el número aleatorio generado.
intento3 = int(input("Ingrese su tercer intento: "))
if intento3 == numero_aleatorio:
    print("¡Felicidades! Has adivinado el número aleatorio.")
else:
    print(f"Lo siento, no has adivinado el número aleatorio. El número era: {numero_aleatorio}. ¡Inténtalo de nuevo!")


