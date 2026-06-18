# Sistema de Inventario y Reposición
# Programa para controlar automáticamente el inventario de una empresa

# Listas para guardar la información de los productos
codigos = []
nombres = []
stocks_actuales = []
stocks_minimos = []
precios_unitarios = []
estados = []
valores_inventario = []


def evaluar_producto(stock_actual, stock_minimo, precio_unitario):

    
    # Determinar estado
    if stock_actual < stock_minimo:
        estado = "Estado Crítico"
    else:
        estado = "Estado Normal"
    
    # Calcular valor del inventario
    valor_inventario = stock_actual * precio_unitario
    
    return estado, valor_inventario


def registrar_producto():

    
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    
    # Validar stock actual
    while True:
        try:
            stock_actual = float(input("Stock actual: "))
            if stock_actual >= 0:
                break
            else:
                print("El stock no puede ser negativo")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    # Validar stock mínimo
    while True:
        try:
            stock_minimo = float(input("Stock mínimo requerido: "))
            if stock_minimo >= 0:
                break
            else:
                print("El stock mínimo no puede ser negativo")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    # Validar precio unitario
    while True:
        try:
            precio_unitario = float(input("Precio unitario ($): "))
            if precio_unitario >= 0:
                break
            else:
                print("El precio no puede ser negativo")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    # Evaluar el producto
    estado, valor = evaluar_producto(stock_actual, stock_minimo, precio_unitario)
    
    # Guardar en las listas
    codigos.append(codigo)
    nombres.append(nombre)
    stocks_actuales.append(stock_actual)
    stocks_minimos.append(stock_minimo)
    precios_unitarios.append(precio_unitario)
    estados.append(estado)
    valores_inventario.append(valor)
    
    print(f"\nProducto registrado: {nombre}")
    print(f"Estado: {estado}\n")


def generar_informe():

    
    if len(codigos) == 0:
        print("\nNo hay productos registrados")
        return
    
    # Cantidad total de productos
    cantidad_total = len(codigos)
    
    # Valor total del inventario
    valor_total = sum(valores_inventario)
    
    # Cantidad de productos críticos
    cantidad_criticos = estados.count("Estado Crítico")
    
    # Porcentaje de productos críticos
    if cantidad_total > 0:
        porcentaje_criticos = (cantidad_criticos / cantidad_total) * 100
    else:
        porcentaje_criticos = 0
    
    # Producto con mayor valor almacenado
    mayor_valor = max(valores_inventario)
    indice_mayor = valores_inventario.index(mayor_valor)
    nombre_mayor = nombres[indice_mayor]
    
    # Producto con menor valor almacenado
    menor_valor = min(valores_inventario)
    indice_menor = valores_inventario.index(menor_valor)
    nombre_menor = nombres[indice_menor]
    
    # Mostrar informe
    print("\n" + "="*70)
    print("INFORME DE INVENTARIO Y REPOSICIÓN")
    print("="*70)
    print(f"Cantidad total de productos: {cantidad_total}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Cantidad de productos críticos: {cantidad_criticos}")
    print(f"Porcentaje de productos críticos: {porcentaje_criticos:.2f}%")
    print(f"\nProducto de mayor valor almacenado: {nombre_mayor} (${mayor_valor:.2f})")
    print(f"Producto de menor valor almacenado: {nombre_menor} (${menor_valor:.2f})")
    print("="*70 + "\n")
    
    # Mostrar detalle de cada producto
    print("DETALLE DE PRODUCTOS:")
    print("-"*70)
    for i in range(len(codigos)):
        print(f"\nCódigo: {codigos[i]}")
        print(f"Nombre: {nombres[i]}")
        print(f"Stock actual: {stocks_actuales[i]:.0f} unidades")
        print(f"Stock mínimo: {stocks_minimos[i]:.0f} unidades")
        print(f"Precio unitario: ${precios_unitarios[i]:.2f}")
        print(f"Estado: {estados[i]}")
        print(f"Valor del inventario: ${valores_inventario[i]:.2f}")
    
    print("\n" + "-"*70 + "\n")


# Programa principal
def main():
    """
    Función principal que controla el flujo del programa.
    """
    
    print("SISTEMA DE INVENTARIO Y REPOSICIÓN")
    print("==================================\n")
    
    while True:
        opcion = input("¿Desea registrar un nuevo producto? (si/no): ").lower()
        
        if opcion == "si" or opcion == "s":
            print()
            registrar_producto()
        elif opcion == "no" or opcion == "n":
            break
        else:
            print("Por favor, ingrese 'si' o 'no'\n")
    
    # Generar informe final
    generar_informe()


# Ejecutar el programa
if __name__ == "__main__":
    main()