#Uso de while con contador, se detendra ala momento que el contador llegue a 5
contador = 0
while contador < 5:
    print(contador)
    contador += 1
  
#Ejemplo de uso de while con booleano, se detendra cuando se cumpla la condicion y activo se vuelva False   
activo = True
while activo:
    entrada = input("Escribe salir para terminar.")
    if entrada == "salir":
        activo = False
