#Precios del Menu
#Comida
vegana = 8000
tradicional = 10000
#Bebida
fria = 2000
caliente = 3000
#Postre
simple = 4000
premium = 6000
total = 0
#Zona de inputs
print("Bienvenido al restaurante, por favor seleccione su comida:")
comida = input("¿Desea comida vegana o tradicional? ").lower()
match comida:
    case "vegana":
        total = total + vegana
    case "tradicional":
        total = total + tradicional
    case _:
        print("Opción no válida, por favor seleccione vegana o tradicional.")
print("¿Desea una bebida fría o caliente?")
bebida = input("Ingrese su bebida: ").lower()       
match bebida:
    case "fria":
        total = total + fria
    case "caliente":
        total = total + caliente
    case _:
        print("Opción no válida, por favor seleccione fría o caliente.")

print("¿Desea un postre simple o premium?")
postre = input("Ingrese su postre: ").lower()
match postre:
    case "simple":
        total = total + simple
    case "premium":
        total = total + premium
    case _:
        print("Opción no válida, por favor seleccione simple o premium.")
if total > 12000:
    print("¡Felicidades! Ha ganado un descuento del 10% en su pedido.")
    total = total * 0.9
print(f"El total de su pedido es: {total}")