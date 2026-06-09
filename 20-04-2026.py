clp = float(input("Ingrese la cantidad de dinero a ingresar: (En pesos chilenos)"))
dolar = float(input("Ingrese el tipo de cambio a dolar:"))
euro = float(input("Ingrese el tipo de cambio a euro:"))
dolar_convertido = clp / dolar
euro_convertido = clp / euro
print(f"La cantidad de dinero ingresada en pesos chilenos es: {clp:,.0f}")
print(f"La cantidad de dinero ingresada en dolares es: {dolar_convertido:,.2f}")
print(f"La cantidad de dinero ingresada en euros es: {euro_convertido:,.2f}")
