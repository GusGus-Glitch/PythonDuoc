esarf = input("Ingrese su frase al reves: ").strip()
palabras = esarf.split()

p1 = palabras[0][::-1] if len(palabras) > 0 else ""
p2 = palabras[1][::-1] if len(palabras) > 1 else ""
p3 = palabras[2][::-1] if len(palabras) > 2 else ""
p4 = palabras[3][::-1] if len(palabras) > 3 else ""
p5 = palabras[4][::-1] if len(palabras) > 4 else ""

frase_unida = " ".join([p1, p2, p3, p4, p5]).strip()

if len(frase_unida) > 0:
    frase = f"{frase_unida[0].upper()}{frase_unida[1:].lower()}"
    print(f"Original: {frase}")
else:
    print("No ingresaste ninguna palabra.")