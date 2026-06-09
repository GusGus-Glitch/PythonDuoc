p = float(input("Ingrese el capital inicial: "))
r = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
t = float(input("Ingrese el tiempo en años: "))
n = 12
A = p * (1 + (r / 100)/n) ** ( n * t )
print ("Capital final: ", A)
print ("Interés ganado: ", A - p)