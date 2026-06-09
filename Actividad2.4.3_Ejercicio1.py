totalIngresos = 0
print ("Bienvenido al programa de venta de pasajes.")
try:
    cantidad_pasajes = int(input("Ingrese la cantidad de pasajes que desea comprar: "))
except ValueError:
    print("Error: La cantidad de pasajes debe ser un número entero.")
    exit()
for i in range (cantidad_pasajes):
    try:
        valor_pasaje = int(input(f"Ingrese el valor del pasaje nro. {i+1}: "))
        totalIngresos += valor_pasaje

    except ValueError:
        print("Error: El valor del pasaje debe ser un número entero.")
        break
        
if i < cantidad_pasajes - 1:
    print("Error: No se ingresaron todos los valores de los pasajes.")
else:
    print(f"El total de ingresos por la venta de pasajes es: {totalIngresos}.")