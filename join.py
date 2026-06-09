frase = input("Ingrese una frase: ")
frase = frase.split()
if len(frase) > 3:
    print("-".join(frase))
else: 
    print(frase)