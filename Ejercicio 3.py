#Zona de variables
ori = float(input("Cual es el precio original?")) #Se pide el precio original
desc1 = float(input("Cual es el primer descuento?")) #Se pide el primer descuento
desc2 = float(input("Cual es el segundo descuento?")) #Se pide el segundo descuento
#Zona de calculos
remove1 = ori * ( desc1 / 100)
precio1 = ori - remove1
remove2 = precio1 * (desc2 / 100)
precio2 = precio1 - remove2
desctotal = remove1 + remove2
#Zona de prints
print ("El precio original es: ", ori) #Se muestra el precio original
print ("El precio despues del primer descuento es:", precio1) #Mostramos el precio luego del primer descuento
print ("El precio final es:", precio2) #Mostramos el precio luego de todas las operaciones
print ("El monto total descontado es: ", desctotal) #Mostramos los removes sumados