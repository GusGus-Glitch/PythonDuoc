#Zona de inputs
edad = input("Ingrese su edad: ")
ing_mensual = input("Ingrese su ingreso mensual: ")
h_c = input("Ingrese su historial crediticio (bueno/malo): ").lower()
endeudamiento = input("Ingrese su porcentaje de endeudamiento: ")
#Zona de condicionales
Good = 0
#Ingresos
if ing_mensual > "1500000":
    Good = Good + 1
else:   
    Good = Good
#Historial crediticio
if h_c == "bueno":
    Good = Good + 1
elif h_c == "malo":
    Good = Good
#Endeudamiento
if endeudamiento < "30":
    Good = Good + 1
else:
    Good = Good
#Calculo del riesgo
if Good == 1: 
    Riesgo = "Alto"
elif Good == 2:
    Riesgo = "Medio"
elif Good == 3:
    Riesgo = "Bajo"
if edad < "21" or edad > "70" and Riesgo == "Bajo":
    Riesgo = "Medio" 
#Zona de outputs
print("El riesgo de crédito es: ", Riesgo)