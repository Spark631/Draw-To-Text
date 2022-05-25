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
drawn = False
def draw_grid(screen, width, height):
    for x in range(0, width, 40):
        pygame.draw.line(screen, (255, 255, 0), (x, 0), (x, height))
    for y in range(0, height, 40):
        pygame.draw.line(screen, (255, 255, 0), (0, y), (width, y))

def draw_boxes(screen, width, height):
    for i in range(rows):
        for j in range(columns):
            pygame.draw.rect(screen, (0, 255, 0), (i * 40, j * 40, 40, 40))
            boxes.append((screen, [0, 255, 0], (i * 40, j * 40, 40, 40)))
    return boxes

def hand_draw(screen, width, height):
    for box in boxes:
        if box[1] == [255, 0, 0]:
            pygame.draw.rect(screen, (255, 0, 0), box[2])
    pass

counter = 0

while active:

    cursor = pygame.mouse.get_pos()
            
    if drawn == False:
        draw_boxes(screen, width, height)
        draw_grid(screen, width, height)
        drawn = True
        
    hand_draw(screen, width, height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            dicty = {}
            if event.key == pygame.K_SPACE:
                with open("grid.txt", "w", encoding="utf-8") as f:
                    for i, box in enumerate(boxes):

                        # This is basically creating the outline of the dictionary
                        if i < 20:

                            # If the box is red, then we will add it to the dictionary as an " O "
                            if box[1] == [255, 0, 0]:
                                dicty[i] = "😈"
                            else:
                                # If the box is green, then we will add it to the dictionary as an " X "
                                dicty[i] = "😇"
                        else:
                            # This is resetting the counter so then values over 20 can be added to the dictionary
                            if counter == 20:
                                counter = 0

                            if box[1] == [255, 0, 0]:
                                dicty[counter] += "😈"
                            else:
                                dicty[counter] += "😇"

                            counter += 1

                    for i in dicty:
                        f.write((dicty[i]) + "\n")

        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if pygame.Rect(box[2]).collidepoint(cursor):
                    box[1][0] = 255
                    box[1][1] = 0

    pygame.display.update()
    pygame.display.flip()
