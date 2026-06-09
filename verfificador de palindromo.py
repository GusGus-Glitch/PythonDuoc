#Usar for para recorrer un numero entregadp y verificar si es palindromo o no
print("Verificaremos si su numero es palindromo o no.")
numero = int(input("Ingrese un numero: "))
cantidad = len(str(numero))
for i in range(cantidad):
    if str(numero) == str(numero)[::-1]:
        print("Su numero es palindromo.")
        break
    else:
        print("Su numero no es palindromo.")
        break