#Comenzamos con las directrices para el menu
print ("A continuacion se haran distfloatas operaciones matematicas.") #prints para dar contexto al usuario
print ("Primero comenzaremos con la suma.")
sum1 = float(input("Ingrese el primer numero de la suma:")) # Primer input para registrar primer numero a sumar
sum2 = float(input("Ingrese el segundo numero de la suma:")) #Segundo input de suma
print ("A continuacion seguiremos con la resta.") #Contexto para el usuario
rest1 = float(input("Ingrese el primer numero para restar:"))#Pedimos el primer numero para restar
rest2 = float(input("Ingrese el segundo numero de la resta:"))#Pedimos segundo numero para la resta
print ("Ahora continuamos con la multiplicacion.")#Contexto para el usuario
mult1 = float(input("Ingrese el primer numero a multiplicar:")) #Pedimos el primer numero de la multi.
mult2 = float(input("Ingrese el segundo numero a multiplicar:"))#Pedimos el numero para multiplicar
print ("Ahora ingrese los numeros para dividir.") #Contexto para el usuario
div1 = float(input("Ingrese el primer numero para dividir:"))#Primer numero a dividir
div2 = float(input("Ingrese el segundo numero a dividir:"))#Segundo numero a dividir.
print ("Ahora sacaremos la raiz cuadrada de 2 numeros.")#Contexto para el usuario
raiz1 = float(input("Ingrese el primer numero a sacar raiz cuadrada:"))#primer numero para sacar raiz
raiz2 = float(input("Ingrese el segundo numero a sacar raiz cuadrada:"))#segundo numero a sacar raiz
print ("Ahora por ultimo sacaremos el exponente de un numero.")
exp1 = float(input("Ingrese el numero para la operacion:"))
exp2 = float(input("Ahora ingrese el exponente:"))
#####Ahora haremos una seccion para los calculos######
sum = sum1 + sum2 #Sumas
rest = rest1 - rest2#restas
mult = mult1 + mult2#multiplicaciones
div= div1 / div2#divisiones
resraiz1 = raiz1 ** 0.5#Aqui sacamos las raices
resraiz2 = raiz2 ** 0.5#Lo hacemos utilizando de exponente 0.5
exp = exp1 ** exp2 #El "**" simboliza para sacar exponente del numero
#Ahora haremos el menu de salida segun la rubrica
#Ahora devolvemos solo los resultados al usuario, sin mostrar los numeros que se ingresaron, solo el resultado de cada operacion.
print ("----------------------Resultados----------------------") #Menu de salida para el usuario
print ("----------------------Suma----------------------")  
print ("El resultado de la suma es:", sum)
print ("----------------------Resta----------------------")
print ("El resultado de la resta es:", rest)
print ("----------------------Multiplicacion----------------------")
print ("El resultado de la multiplicacion es:", mult)
print ("----------------------Division----------------------")
print ("El resultado de la division es:", div)
print ("----------------------Raiz Cuadrada----------------------")
print ("El resultado de la raiz cuadrada del primer numero es:", resraiz1)
print ("El resultado de la raiz cuadrada del segundo numero es:", resraiz2)
print ("----------------------Exponente----------------------")
print ("El resultado del exponente es:", exp)
print ("----------------------Cuestionario de satisfaccion----------------------")
nombre =  (str(input("¿Cual es su nombre?"))) #Cuestionario de satisfaccion para el usuario
nota = (int(input("Califique del 1 al 10 el programa:")))#Cuestionario de satisfaccion para el usuario
comentario = (str(input("Describa el por que de su clasificacion: "))) #Cuestionario de satisfaccion para el usuario





print ("----------------------Resultados----------------------") #Menu de salida para el usuario
print ("----------------------Suma----------------------")
print ("El resultado de la suma entre ", sum1, "y", sum2, "es:", sum)
print ("----------------------Resta----------------------")
print ("El resultado de la resta entre ", rest1, "y", rest2, "es:", rest)
print ("----------------------Multiplicacion----------------------")
print ("El resultado de la multiplicacion entre ", mult1, "y", mult2, "es:", mult)
print ("----------------------Division----------------------")
print ("El resultado de la division entre ", div1, "y", div2, "es:", div)
print ("----------------------Raiz Cuadrada----------------------")
print ("El resultado de la raiz cuadrada de ", raiz1, "es:", resraiz1)
print ("El resultado de la raiz cuadrada de ", raiz2, "es:", resraiz2)
print ("----------------------Exponente----------------------")
print ("El resultado de ", exp1, "elevado a ", exp2, "es:", exp)
print ("----------------------Cuestionario de satisfaccion----------------------")
print ("El nombre del usuario es:", nombre) 
print ("La nota que el usuario dio al programa es:", nota)
print ("El comentario del usuario es:", comentario)
print ("----------------------Fin del programa----------------------")
