import pygame, sys
from pygame.locals import *
from funciones import *
from config import *
from sound import *
import random
import csv

pygame.init()

# configuro fuente del contador de monedas
score = 0
font = pygame.font.Font(None, 50) # fuente del texto
text_score = font.render(f"Level: 1   Score : {score}", True, BLACK)
text_rect = text_score.get_rect()

# Lista para almacenar las posiciones de los segmentos de la serpiente
snake_segments = [get_rectangulo(x, y, rect_width, rect_height, RED)]

    
    
count_comer = 0
coin_dict = {
    "x" : 300,
    "y" : 300
    }

#vida imagen 
imagen_vida = pygame.image.load("PICKUP_VIDA.png")
vida_imagen = pygame.transform.scale(imagen_vida,(45,45))

vida_snake = 3 

imagen_enemigo = pygame.image.load("enemigo.png")
enemigo_imagen = pygame.transform.scale(imagen_enemigo,(50,50))
rect_enemigo = pygame.Rect(600,400,50,50)
enemigo_vivo = True 
x_enemigo = 600 
y_enemigo = 400


# Bucle principal
run = True
clock = pygame.time.Clock()
menu_estado = "menu"
ingresando_nombre = True


while run:
    #detectar los eventos
    # MENU JUEGO 
    if menu_estado =="menu":
        menu_inicio(font)
        for event in pygame.event.get():
            if event.type == QUIT: 
                run = False
            keys = pygame.key.get_pressed()
            if keys[K_ESCAPE]:
                menu_estado = "jugar"
                sound.play()
                sound.set_volume(volumen_inicial)
            if keys[K_q]:  # Si se presiona la tecla 'q', se sale del juego
                run = False
        
    
    # Actualizar la pantalla
    pygame.display.flip()
    #FIN DEL JUEGO  
    if menu_estado == "game over": 

        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        sound.stop()

        nombre = ""
        if(ingresando_nombre):
            nombre = cargar_nombre(font)
            ingresando_nombre = False

        
###########Guardar puntajes ###########
        if(guardar_puntaje):
                guardar_puntajes("puntajes.csv", nombre, score)
                guardar_puntaje = False

        puntajes = cargar_score()
        mostrar_tabla(puntajes, font)
        
#JUEGO 
    if  menu_estado == "jugar":
        for event in pygame.event.get():
                    
            if event.type == QUIT:  #Evento de cierre de ventana del juego
                run = False
            keys = pygame.key.get_pressed()
            if keys [K_ESCAPE]:
                menu_estado = "menu"
            if keys[K_UP] and snake_direction != 1:
                snake_direction = 0  # Cambia la dirección hacia arriba
            elif keys[K_DOWN] and snake_direction != 0:
                snake_direction = 1  # Cambia la dirección hacia abajo
            elif keys[K_LEFT] and snake_direction != 3:
                snake_direction = 2  # Cambia la dirección hacia la izquierda
            elif keys[K_RIGHT] and snake_direction != 2:
                snake_direction = 3

        
            
        # Obtén la cabeza de la serpiente
        
        snake_head = snake_segments[0]["rect"]

    # Actualiza la posición de la serpiente
        new_head = movimiento_serpiente(snake_segments, snake_direction)
        snake_segments[0] = new_head 
        
        # Verificar colisión con la pared

        if (new_head["rect"].left < 0 or new_head["rect"].right > WIDTH or new_head["rect"].top < 0 or new_head["rect"].bottom > HEIGHT):
            vida_snake -= 1
            if vida_snake == 0:
                menu_estado = "game over"
            snake_length = 2
            snake_segments[0]["rect"].center = (WIDTH // 2, HEIGHT // 2)
        
        coin_rect = pygame.Rect(coin_dict['x'], coin_dict['y'], 25, 25)  # Rectángulo de la moneda actual

        if (colision_2_rect(coin_rect,new_head["rect"])):

            score += 1
            text_score = font.render(f"Level:  1  Score = {score}", True, BLACK)
            coin_dict['x'] = random.randint(0, WIDTH - 25)  # Mueve la moneda a una nueva ubicación
            coin_dict['y'] = random.randint(0, HEIGHT - 25)  # Mueve la moneda a una nueva ubicación
            snake_length += 1  # Aumenta la longitud de la serpiente
        
        if ( colision_2_rect(rect_enemigo,new_head["rect"])):
            if(vida_snake == 0):
                menu_estado = "game over"
            else:
                vida_snake -= 1
                x_enemigo = random.randint(0,750)
                y_enemigo = random.randint(100,550)
                rect_enemigo.x = x_enemigo
                rect_enemigo.y = y_enemigo
        
        current_time = pygame.time.get_ticks()
    
        if current_time > colision:
            for segment in snake_segments[1:]:  # Comenzamos desde el segundo segmento ya que la cabeza no puede chocar consigo misma
                if colision_2_rect(segment["rect"], snake_segments[0]["rect"]):
                    run = False
                    break

        
        # Agrega el nuevo segmento de cabeza
        
        snake_segments.insert(0, {"rect": pygame.Rect(new_head["rect"]), "dir": snake_direction})

        # Elimina el último segmento de la serpiente
        
        if len(snake_segments) > snake_length:
            del snake_segments[-1]
        
        text_rect.center = (WIDTH // 2, 15) 
        
        #screen.fill(BLACK)
        screen.blit(wallpaper, (0, 0))

        for segment in snake_segments:
            pygame.draw.rect(screen, RED, segment["rect"], 0)
        
        screen.blit(text_score, text_rect)
        
        screen.blit(coin_images, (coin_dict['x'], coin_dict['y'])) # dibuja los coins
        
        # Dibuja la serpiente
        for i, segment in enumerate(snake_segments):
            if i == 0:
                # Dibuja la cabeza de la serpiente
                screen.blit(cabeza_imagen, segment["rect"])
        
        for i in range(vida_snake):
            screen.blit(vida_imagen,(55 + 35 * i, 50))
        if enemigo_vivo:
            screen.blit(enemigo_imagen,(x_enemigo,y_enemigo))

    pygame.display.flip()
    clock.tick(10)

    
pygame.quit()
sys.exit()
