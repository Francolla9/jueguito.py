import pygame
from config import *
import csv

def colision_2_rect(rect1, rect2):
    return rect1.colliderect(rect2) # Verifica si dos rectángulos se superponen

def get_rectangulo(x, y, width, height, color):
    rect = pygame.Rect(x, y, width, height)  #Crea un rectángulo con propiedades personalizadas
    surface = pygame.Surface(rect.size, pygame.SRCALPHA)
    pygame.draw.rect(surface, color, rect, 0)
    return {
        "rect": rect,
        "surface": surface,
        "dir": 0
    }

def menu_inicio(font):
    screen.fill(BLACK)
    text_surface_welcome = font.render("¡Bienvenido!", True, CYAN)
    text_rect_welcome = text_surface_welcome.get_rect(center=(WIDTH // 2, HEIGHT // 6.5))
    text_surface_continue = font.render("Continuar al juego(""Presione esc"")", True, RED)
    text_rect_continue = text_surface_continue.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    text_surface_exit = font.render("Salir del juego (""presione q"")", True, GREEN)
    text_rect_exit = text_surface_exit.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
        
    screen.blit(text_surface_welcome, text_rect_welcome)    
    screen.blit(text_surface_continue, text_rect_continue)
    screen.blit(text_surface_exit, text_rect_exit)

def movimiento_serpiente(serpiente , snake_direction):
        new_head = 0
        if snake_direction == 0:
            new_head = {
                "rect": pygame.Rect(
                    serpiente[0]["rect"].left,
                    serpiente[0]["rect"].top - (snake_speed + segment_spacing),
                    rect_width,
                    rect_height,
                ),
                "dir": snake_direction,
            }
        elif snake_direction == 1:
            new_head = {
                "rect": pygame.Rect(
                    serpiente[0]["rect"].left,
                    serpiente[0]["rect"].top + (snake_speed + segment_spacing),
                    rect_width,
                    rect_height,
                ),
                "dir": snake_direction,
            }
        elif snake_direction == 2:
            new_head = {
                "rect": pygame.Rect(
                    serpiente[0]["rect"].left - (snake_speed + segment_spacing),
                    serpiente[0]["rect"].top,
                    rect_width,
                    rect_height,
                ),
                "dir": snake_direction,
            }
        elif snake_direction == 3:
            new_head = {
                "rect": pygame.Rect(
                    serpiente[0]["rect"].left + (snake_speed + segment_spacing),
                    serpiente[0]["rect"].top,
                    rect_width,
                    rect_height,
                ),
                "dir": snake_direction,
            }
        return new_head

def guardar_puntajes(nombre_archivo, nombre, puntos)->None:
    with open(nombre_archivo, 'a', newline='',encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([nombre, puntos])

def cargar_nombre(font):

    nombre = ""
    escribiendo = True

    while escribiendo:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.key == pygame.K_RETURN:
                    escribiendo = False
                else:
                    caracter = event.unicode
                    nombre += caracter
        
        screen.fill((0, 0, 0))
        
        texto = font.render("Nombre: " + nombre, True, BLANCO)
        
        texto_rect = texto.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        
        screen.blit(texto, texto_rect)

        pygame.display.flip()

    return nombre

def cargar_score():
    puntajes = []
    with open("puntajes.csv", 'r') as archivo:
        lector = csv.reader(archivo)
        
        for linea in lector:
            nombre = linea[0]
            puntaje = int(linea[1])
            puntajes.append([nombre, puntaje])

    puntajes.sort(key=lambda x: x[1], reverse=True)
    
    return puntajes[:5]

def mostrar_tabla(puntajes,font):
    screen.fill(BLACK)
    y = 100
    
    fin_del_juego = font.render("GAME OVER", True, RED)
    screen.blit(fin_del_juego,(200, 200))
    nombres = font.render("TOP 5", True, BLANCO)
    rect_nombre = nombres.get_rect(center=(screen.get_width() // 1.25, y))
    screen.blit(nombres, rect_nombre)

    for indice, jugador in enumerate(puntajes):
        y += 40
        nombre = jugador[0]
        puntaje = jugador[1]
        
        texto_nombre = font.render(nombre, True, BLANCO)
        rect_nombre = texto_nombre.get_rect(center=(screen.get_width() // 1.25, y))
        screen.blit(texto_nombre, rect_nombre)
        
        texto_puntaje = font.render(str(puntaje), True, BLANCO)
        rect_puntaje = texto_puntaje.get_rect(right=screen.get_width() - 50, centery=y)
        screen.blit(texto_puntaje, rect_puntaje)
        
        
    pygame.display.flip()
