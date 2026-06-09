print ("Calculadora de IMC")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
dif_minima = imc - 18.5
dif_maxima = imc - 24.9
print("Su IMC es:", imc)
print("Diferencia con el límite inferior (18.5):", dif_minima)
print("Diferencia con el límite superior (24.9):", dif_maxima)