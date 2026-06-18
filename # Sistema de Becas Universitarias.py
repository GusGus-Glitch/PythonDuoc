estudiantes = []
becas_asignadas = []

def evaluar_beca(nombre, promedio, asistencia, ingreso):

    # Verificar si tiene derecho a beca completa
    if promedio >= 6.0 and asistencia >= 90 and ingreso < 800000:
        tipo_beca = "Beca Completa"
    
    # Verificar si tiene derecho a beca parcial
    elif promedio >= 5.5 and asistencia >= 80 and ingreso < 1500000:
        tipo_beca = "Beca Parcial"
    
    # Si no cumple, no tiene beca
    else:
        tipo_beca = "Sin Beca"
    
    return tipo_beca


def registrar_estudiante():
    
    nombre = input("Nombre del estudiante: ")
    
    # Validar promedio
    while True:
        try:
            promedio = float(input("Promedio de notas (1.0 a 7.0): "))
            if 1.0 <= promedio <= 7.0:
                break
            else:
                print("El promedio debe estar entre 1.0 y 7.0")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    # Validar asistencia
    while True:
        try:
            asistencia = float(input("Porcentaje de asistencia (0 a 100): "))
            if 0 <= asistencia <= 100:
                break
            else:
                print("La asistencia debe estar entre 0 y 100")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    # Validar ingreso
    while True:
        try:
            ingreso = float(input("Ingreso familiar mensual ($): "))
            if ingreso >= 0:
                break
            else:
                print("El ingreso no puede ser negativo")
        except ValueError:
            print("Por favor, ingrese un número válido")
    
    # Evaluar la beca
    beca = evaluar_beca(nombre, promedio, asistencia, ingreso)
    
    # Guardar los datos en las listas
    estudiantes.append({
        "nombre": nombre,
        "promedio": promedio,
        "asistencia": asistencia,
        "ingreso": ingreso
    })
    becas_asignadas.append(beca)
    
    print(f"\nEstudiante registrado: {nombre}")
    print(f"Beca asignada: {beca}\n")


def generar_reporte():
    
    if len(estudiantes) == 0:
        print("\nNo hay estudiantes registrados")
        return
    
    # Contar becas
    cantidad_completas = becas_asignadas.count("Beca Completa")
    cantidad_parciales = becas_asignadas.count("Beca Parcial")
    cantidad_sin_beca = becas_asignadas.count("Sin Beca")
    
    # Mostrar reporte
    print("\n" + "="*50)
    print("REPORTE DE BECAS UNIVERSITARIAS")
    print("="*50)
    print(f"Cantidad de estudiantes evaluados: {len(estudiantes)}")
    print(f"Cantidad de becas completas: {cantidad_completas}")
    print(f"Cantidad de becas parciales: {cantidad_parciales}")
    print(f"Cantidad sin beca: {cantidad_sin_beca}")
    print("="*50 + "\n")
    
    # Mostrar detalle de cada estudiante
    print("DETALLE DE ESTUDIANTES:")
    print("-"*50)
    for i in range(len(estudiantes)):
        est = estudiantes[i]
        print(f"\nEstudiante: {est['nombre']}")
        print(f"  Promedio: {est['promedio']}")
        print(f"  Asistencia: {est['asistencia']}%")
        print(f"  Ingreso familiar: ${est['ingreso']:.0f}")
        print(f"  Beca asignada: {becas_asignadas[i]}")
    
    print("\n" + "="*50 + "\n")


# Programa principal
def main():
    
    print("SISTEMA DE BECAS UNIVERSITARIAS")
    print("================================\n")
    
    while True:
        opcion = input("¿Desea registrar un nuevo estudiante? (si/no): ").lower()
        
        if opcion == "si" or opcion == "s":
            registrar_estudiante()
        elif opcion == "no" or opcion == "n":
            break
        else:
            print("Por favor, ingrese 'si' o 'no'\n")
    
    # Generar reporte final
    generar_reporte()


# Ejecutar el programa
if __name__ == "__main__":
    main()