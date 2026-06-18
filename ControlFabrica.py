
# Listas para guardar los datos
dias = []
producciones = []
categorias = []


def clasificar_produccion(produccion):

    
    if produccion > 1000:
        categoria = "Producción Alta"
    elif 500 <= produccion <= 1000:
        categoria = "Producción Media"
    else:
        categoria = "Producción Baja"
    
    return categoria


def registrar_produccion(numero_dias):

    
    for dia in range(1, numero_dias + 1):
        while True:
            try:
                produccion = float(input(f"Producción del día {dia}: "))
                if produccion >= 0:
                    break
                else:
                    print("La producción no puede ser negativa")
            except ValueError:
                print("Por favor, ingrese un número válido")
        
        # Clasificar la producción
        categoria = clasificar_produccion(produccion)
        
        # Guardar en las listas
        dias.append(dia)
        producciones.append(produccion)
        categorias.append(categoria)


def analizar_produccion():

    
    if len(producciones) == 0:
        print("\nNo hay datos registrados")
        return
    
    # Calcular producción total
    produccion_total = sum(producciones)
    
    # Calcular producción promedio
    produccion_promedio = produccion_total / len(producciones)
    
    # Encontrar día con mayor producción
    mayor_produccion = max(producciones)
    dia_mayor = dias[producciones.index(mayor_produccion)]
    
    # Encontrar día con menor producción
    menor_produccion = min(producciones)
    dia_menor = dias[producciones.index(menor_produccion)]
    
    # Contar categorías
    cantidad_alta = categorias.count("Producción Alta")
    cantidad_media = categorias.count("Producción Media")
    cantidad_baja = categorias.count("Producción Baja")
    
    # Mostrar reporte
    print("\n" + "="*60)
    print("ANÁLISIS DE PRODUCCIÓN DE LA FÁBRICA")
    print("="*60)
    print(f"Número de días analizados: {len(producciones)}")
    print(f"Producción total: {produccion_total:.0f} unidades")
    print(f"Producción promedio: {produccion_promedio:.2f} unidades")
    print(f"\nDía con mayor producción: Día {dia_mayor} con {mayor_produccion:.0f} unidades")
    print(f"Día con menor producción: Día {dia_menor} con {menor_produccion:.0f} unidades")
    print(f"\nCantidad de días con Producción Alta: {cantidad_alta}")
    print(f"Cantidad de días con Producción Media: {cantidad_media}")
    print(f"Cantidad de días con Producción Baja: {cantidad_baja}")
    print("="*60 + "\n")
    
    # Mostrar detalle de cada día
    print("DETALLE POR DÍA:")
    print("-"*60)
    for i in range(len(producciones)):
        print(f"Día {dias[i]}: {producciones[i]:.0f} unidades - {categorias[i]}")
    
    print("-"*60 + "\n")


# Programa principal
def main():
    """
    Función principal que controla el flujo del programa.
    """
    
    print("CONTROL DE PRODUCCIÓN DE UNA FÁBRICA")
    print("====================================\n")
    
    # Solicitar cantidad de días
    while True:
        try:
            numero_dias = int(input("¿Cuántos días desea analizar? "))
            if numero_dias > 0:
                break
            else:
                print("Debe ingresar un número positivo")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    print()
    
    # Registrar producción de cada día
    registrar_produccion(numero_dias)
    
    # Analizar y mostrar reporte
    analizar_produccion()


# Ejecutar el programa
if __name__ == "__main__":
    main()