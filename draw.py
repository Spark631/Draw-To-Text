import pygame
import sys
import random

pygame.init()

width, height = 800, 800
pygame.display.set_caption("DTT")
screen = pygame.display.set_mode((width, height))

rows = 20
columns = 20

active = True

boxes = []

def draw_grid(screen, width, height):
    for x in range(0, width, 40):
        pygame.draw.line(screen, (255, 255, 0), (x, 0), (x, height))
    for y in range(0, height, 40):
        pygame.draw.line(screen, (255, 255, 0), (0, y), (width, y))

def draw_boxes(screen, width, height):
    for i in range(rows):
        for j in range(columns):
            pygame.draw.rect(screen, (0, 255, 0), (i * 40, j * 40, 40, 40))
            boxes.append((i * 40, j * 40, 40, 40))
    return boxes

while active:
    
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            pygame.quit()
            sys.exit()
    # print(draw_boxes(screen, width, height))
    draw_boxes(screen, width, height)
    draw_grid(screen, width, height)
    pygame.display.flip()
