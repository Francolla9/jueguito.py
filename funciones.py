import pygame
import random

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


