import pygame
import random

# Configuración inicial
pygame.init()
TAMANO_CUADRO = 20
ANCHO, ALTO = 600, 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Colores
NEGRO, BLANCO, VERDE, ROJO = (20, 20, 20), (255, 255, 255), (0, 255, 100), (255, 50, 50)

# Estado del juego
serpiente = [[100, 100], [80, 100], [60, 100]]
direccion = "DERECHA"
comida = [random.randrange(0, ANCHO, TAMANO_CUADRO), random.randrange(0, ALTO, TAMANO_CUADRO)]
puntuacion = 0

jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: jugando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion != "ABAJO": direccion = "ARRIBA"
            if evento.key == pygame.K_DOWN and direccion != "ARRIBA": direccion = "ABAJO"
            if evento.key == pygame.K_LEFT and direccion != "DERECHA": direccion = "IZQUIERDA"
            if evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA": direccion = "DERECHA"

    # 1. Calcular nueva cabeza
    nueva_cabeza = list(serpiente[0])
    if direccion == "ARRIBA":    nueva_cabeza[1] -= TAMANO_CUADRO
    if direccion == "ABAJO":     nueva_cabeza[1] += TAMANO_CUADRO
    if direccion == "IZQUIERDA": nueva_cabeza[0] -= TAMANO_CUADRO
    if direccion == "DERECHA":   nueva_cabeza[0] += TAMANO_CUADRO

    serpiente.insert(0, nueva_cabeza)

    # 2. Lógica de comida
    if serpiente[0] == comida:
        puntuacion += 1
        comida = [random.randrange(0, ANCHO, TAMANO_CUADRO), random.randrange(0, ALTO, TAMANO_CUADRO)]
    else:
        serpiente.pop() # Elimina la cola si no comió

    # 3. Colisiones (Paredes o cuerpo)
    if (serpiente[0][0] < 0 or serpiente[0][0] >= ANCHO or 
        serpiente[0][1] < 0 or serpiente[0][1] >= ALTO or 
        serpiente[0] in serpiente[1:]):
        jugando = False # Game Over

    # 4. Dibujar
    ventana.fill(NEGRO)
    for pos in serpiente:
        pygame.draw.rect(ventana, VERDE, (pos[0], pos[1], TAMANO_CUADRO-2, TAMANO_CUADRO-2))
    pygame.draw.rect(ventana, ROJO, (comida[0], comida[1], TAMANO_CUADRO, TAMANO_CUADRO))
    
    pygame.display.flip()
    reloj.tick(10) # Controla la dificultad (velocidad)

pygame.quit()