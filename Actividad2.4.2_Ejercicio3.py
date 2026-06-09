try:
    numerador = int(input("Ingrese el numerador: "))
    divisor = int(input("Ingrese el divisor: "))

    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")
    
    resultado = numerador / divisor
    print(f"El resultado de la division es: {resultado}.")

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError as zde:
    print(f"Error: {zde}")
finally:
    print("Fin del programa.")