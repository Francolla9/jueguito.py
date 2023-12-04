import pygame

#Configuración del juego
#Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600


# Configuración de la ventana
window = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Snake")
fondo = pygame.image.load("campo-cesped_1232-1008.png")
wallpaper = pygame.transform.scale(fondo,(WIDTH,HEIGHT)) 
cabeza_imagen = pygame.image.load("0.png")
cabeza_imagen = pygame.transform.scale(cabeza_imagen, (25, 25))
coin_images = pygame.transform.scale(pygame.image.load("1.png"), (25, 25))

#Velocidad de movimiento
snake_speed = 25

#Configuración de la serpiente
snake_length = 2
segment_spacing = 5
rect_width = 25
rect_height = 25


x = WIDTH // 2
y = HEIGHT // 2
snake_direction = 0

#Configuración de las monedas
colision = 1000  # Tiempo en milisegundos para evitar colisiones

#Colores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)