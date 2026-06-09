print ("Ingrese el numero para transformarlo a binario")
numero = int(input())
b7 = (numero // 2 ** 7) % 2
b6 = (numero // 2 ** 6) % 2 
b5 = (numero // 2 ** 5) % 2 
b4 = (numero // 2 ** 4) % 2
b3 = (numero // 2 ** 3) % 2
b2 = (numero // 2 ** 2) % 2
b1 = (numero // 2 ** 1) % 2
b0 = (numero // 2 ** 0) % 2
print (b7, b6, b5, b4, b3, b2, b1, b0)