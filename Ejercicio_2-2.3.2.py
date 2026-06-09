nota = 0
print ("Bienvenido al examen")
print (f"Pregunta numero 1: \n ¿Escoja un adc de piltover? \n A. Twitch \n B. Jax \n C. Caitlyn \n D. Samira")
resp1 = input("Ingrese su respuesta: ")
match resp1:
    case "A":
        print("Respuesta casi buena")
        nota = nota + 0.5
    case "B":
        print("Respuesta incorrecta")
    case "C":
        print("Respuesta correcta")
        nota = nota + 1
    case "D":
        print("Respuesta incorrecta")
print (f"Pregunta numero 2: \n ¿Escoja un tanque de las islas de las sombras? \n A. Maokai \n B. Rammus \n C. Malphite \n D. Hecarim")
resp2 = input("Ingrese su respuesta: ")
match resp2:
    case "A":
        print("Respuesta correcta")
        nota = nota + 1
    case "B":
        print("Respuesta incorrecta")
    case "C":
        print("Respuesta incorrecta")
    case "D":
        print("Respuesta casi buena")
        nota = nota + 0.5
print (f"Pregunta numero 3: \n ¿Escoja un mago de las tierras de Runaterra? \n A. Ryze \n B. Malzahar \n C. Veigar \n D. Brand")
resp3 = input("Ingrese su respuesta: ")
match resp3:
    case "A":
        print("Respuesta correcta")
        nota = nota + 1
    case "B":
        print("Respuesta incorrecta")
    case "C":
        print("Respuesta incorrecta")
    case "D":
        print("Respuesta casi buena")
        nota = nota + 0.5
match nota:
    case 3:
        print(f"Su nota es un 7.0, Felicidades")
    case 2.5:
        print(f"Su nota es un 5.8, Buen trabajo")
    case 2:
        print(f"Su nota es un 4.5, Aprobado por poco, Siga estudiando")
    case 1.5:
        print(f"Su nota es un 3.2, Reprobado, Siga estudiando")
    case 1:
        print(f"Su nota es un 2.0, Reprobado, Siga estudiando")
    case 0.5:
        print(f"Su nota es un 1.0, Reprobado, Siga estudiando")
    case 0:
        print(f"Su nota es un 0.0, Reprobado, Siga estudiando")
