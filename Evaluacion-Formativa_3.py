#Precios
pikachu_roll = 4500
otaku_roll = 5000
pulpo_venenoso_roll = 5200
anguila_electrica_roll = 4800
total = 0
#Definicion
cod = True
estado = True
#Contador
cantidad_pikachu_roll = 0
cantidad_otaku_roll = 0
cantidad_pulpo_venenoso_roll = 0
cantidad_anguila_electrica_roll = 0
cantidad_total = 0
#Bienvenida
print ("Bienvenido a la tienda de delivery de rolls:")
#Proceso de compra
while  estado == True:
    print ("Escoja su producto:\n1. Pikachu Roll\n2. Otaku Roll\n3. Pulpo Venenoso Roll\n4. Anguila Eléctrica Roll")
    opcion = input("Ingrese el número de su opción: ")
    if opcion == "1":
        cantidad_pikachu_roll += 1
        total += pikachu_roll
        print (f"Has seleccionado Pikachu Roll. Precio total: ${total}")
        continuar = input ("¿Desea agregar otro producto? (Si/No): ").lower()
        if continuar == "no":
            estado = False
        elif continuar == "si":
            continue
    elif opcion == "2":
        cantidad_otaku_roll += 1
        total += otaku_roll
        print (f"Has seleccionado Otaku Roll. Precio total: ${total}")
        continuar = input ("¿Desea agregar otro producto? (Si/No): ").lower()
        if continuar == "no":
            estado = False
        elif continuar == "si":
            continue
    elif opcion == "3":
        cantidad_pulpo_venenoso_roll += 1
        total += pulpo_venenoso_roll
        print (f"Has seleccionado Pulpo Venenoso Roll. Precio total: ${total}")
        continuar = input ("¿Desea agregar otro producto? (Si/No): ").lower()
        if continuar == "no":
            estado = False
        elif continuar == "si":
            continue
    elif opcion == "4":
        cantidad_anguila_electrica_roll += 1
        total += anguila_electrica_roll
        print (f"Has seleccionado Anguila Eléctrica Roll. Precio total: ${total}")
        continuar = input ("¿Desea agregar otro producto? (Si/No): ").lower()
        if continuar == "no":
            estado = False
        elif continuar == "si":
            continue
    else:
        print ("Opción no válida. Por favor, ingrese un número válido.")
#Descuento
bul = input (f"El total a pagar es: ${total}\n ¿Desea usar un código de descuento? (Si/No): ").lower()
if bul == "si":
    while cod == True:
     codigo = input ("Ingrese su código de descuento: ")
     if codigo == "soyotaku":
        descuento = total * 0.10
        total -= descuento
        print (f"Código de descuento aplicado.")
        print ("******************************")
        print (f"Cantidad de productos: {cantidad_total}")
        print (f"Pikachu Roll: {cantidad_pikachu_roll}")
        print (f"Otaku Roll: {cantidad_otaku_roll}")
        print (f"Pulpo Venenoso Roll: {cantidad_pulpo_venenoso_roll}")
        print (f"Anguila Eléctrica Roll: {cantidad_anguila_electrica_roll}")
        print ("******************************")
        print (f"Subtpotal a pagar: ${total + descuento}")
        print (f"Descuento aplicado: ${descuento}")
        print (f"Total a pagar: ${total}")
        cod = False
     else:
        intento = input("Código de descuento no válido. ¿Desea intentarlo nuevamente? (Si/No): ").lower()
        if intento == "no":
            cod = False
        elif intento == "si":
            continue
        else:
            print ("Opción no válida. Por favor, ingrese 'Si' o 'No'.")
#Sin descuento
elif bul == "no":
        print (f"Código de descuento aplicado.")
        print ("******************************")
        print (f"Cantidad de productos: {cantidad_total}")
        print (f"Pikachu Roll: {cantidad_pikachu_roll}")
        print (f"Otaku Roll: {cantidad_otaku_roll}")
        print (f"Pulpo Venenoso Roll: {cantidad_pulpo_venenoso_roll}")
        print (f"Anguila Eléctrica Roll: {cantidad_anguila_electrica_roll}")
        print ("******************************")
else:
    print ("Opción no válida. Por favor, ingrese 'Si' o 'No'.")

print ("Gracias por su visita. ¡Que tenga un buen día!")