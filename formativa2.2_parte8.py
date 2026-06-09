entrada = input("Ingrese sus datos (Nombre/Cargo/Empresa/Email/Teléfono): ")
datos = entrada.split("/")
nombre = datos[0].strip().upper()
cargo = datos[1].strip()
empresa = datos[2].strip()
email = datos[3].strip().lower()
telefono = datos[4].strip().replace(" ", "")
cargo_empresa = " | ".join([cargo, empresa])

w = 40

borde = f"+{'─' * (w - 2)}+"

print("\nTarjeta de Presentación:\n")
print(borde)
print(f"│ {nombre:<{w-3}}│")
print(f"│ {cargo_empresa:<{w-3}}│")
print(f"│ {email:<{w-3}}│")
print(f"│ {telefono:<{w-3}}│")
print(borde)