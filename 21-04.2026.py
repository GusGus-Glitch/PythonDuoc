contraseña = "python123"
contrasecreta = input("Introduce la contraseña: ")

if contrasecreta.lower().strip() == contraseña:
    print("¡Contraseña correcta! Bienvenido.")
else:
    print("Contraseña incorrecta. Inténtalo de nuevo.")

