# Diccionario con datos de turistas
turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

# Funcion para buscar turistas por pais
def turistas_por_pais(pais):

    turistas_encontrados = []
    
    for id_turista, datos in turistas.items():

        if datos[1].lower() == pais.lower():
            turistas_encontrados.append(datos[0])
    
    if turistas_encontrados:
        print(turistas_encontrados)
    else:
        print("No hay turistas de ese pais.")

# Funcion para calcular el porcentaje de turistas por mes
def turistas_por_mes(mes):
    """
    Retorna el porcentaje de turistas que visitaron Chile en un mes específico.
    
    Args:
        mes (int): Número del mes (1-12)
    
    Returns:
        float: Porcentaje redondeado a un decimal
    """
    contador_mes = 0
    total_turistas = len(turistas)
    
    for id_turista, datos in turistas.items():
        fecha = datos[2]
        mes_ingreso = int(fecha.split("-")[1])
        
        if mes_ingreso == mes:
            contador_mes += 1
    
    porcentaje = (contador_mes / total_turistas) * 100
    return round(porcentaje, 1)

# funcion para eliminar un turista por nombre
def eliminar_turista():
    """
    Permite eliminar un turista por nombre (sin importar mayúsculas/minúsculas).
    Muestra un mensaje de éxito o error según corresponda.
    """
    nombre_buscar = input("Ingrese nombre del turista a eliminar: ").lower()
    
    for id_turista, datos in list(turistas.items()):
        if datos[0].lower() == nombre_buscar:
            del turistas[id_turista]
            print("Turista eliminado con exito.")
            return
    
    print("Turista no encontrado. No se pudo eliminar.")

# Función principal para ejecutar el programa
def main():
    print("Bienvenido al sistema de gestión de turistas en Chile!")
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")
        
        opcion = input("Ingrese opción: ")
        
        if opcion == "1":
            pais = input("Ingrese pais a buscar: ")
            turistas_por_pais(pais)
        
        elif opcion == "2":
            while True:
                mes = input("Ingrese mes a buscar: ")
                try:
                    mes_num = int(mes)
                    if 1 <= mes_num <= 12:
                        porcentaje = turistas_por_mes(mes_num)
                        print(f"El número de turistas equivale al {porcentaje} % del total.")
                        break
                    else:
                        print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                except ValueError:
                    print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
        
        elif opcion == "3":
            eliminar_turista()
        
        elif opcion == "4":
            print("Programa terminado...")
            break
        
        else:
            print("Debe ingresar una opción válida!!")


if __name__ == "__main__":
    main()  