dias = int(input("Ingrese la cantidad de dias:"))
horas = int(input("Ingrese la cantidad de horas:"))
minutos = int(input("Ingrese la cantidad de minutos:"))

diasseg = dias * 86400
horasseg = horas * 3600
minutosseg = minutos * 60
seg = diasseg + horasseg + minutosseg
print ("La cantidad de segundos son:", seg)