#Inputs
pond1 = float(input("Ingrese la ponderacion para nota 1:"))
pond2 = float(input("Ingrese la ponderacion para nota 2:"))
pond3 = float(input("Ingrese la ponderacion para nota 3:"))              
nota1 = float(input("Ingrese la nota 1:"))
nota2 = float(input("Ingrese la nota 2:"))
nota3 = float(input("Ingrese la nota 3:"))
#Calculos
promediofinal = (nota1 * pond1)+(nota2 * pond2)+(nota3 * pond3)
#Prints
print ("El promedio final es: ", promediofinal)