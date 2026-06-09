#Printea las frutas de la lista, partiendo desde 4
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
#Printea 5 numeros, parte desde el 0
for i in range (5):
    print(i)
#Printea numeros de 2 en 2, hasta su rango 10, el primer numero es de inicio, el segundo es el final y el tercero es el paso
for i in range (2, 10, 2):
    print(i)
#Printea cada letra de la palabra "Hola"
for letra in "Hola":
    print(letra)
#Printea el la fruta y las va contabilizando.
for i, valor in enumerate(frutas):
    print(i, valor)