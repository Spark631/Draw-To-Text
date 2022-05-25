import pygame
import sys

pygame.init()

width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DTT")

rows = 20
columns = 20

active = True

boxes = []
drawn = False

counter = 0

def draw_grid(screen, width, height):
    """
    This draws the grid lines
    First For loop is for the vertical lines
    second For loop is for the horizontal lines
    """
    
    for x in range(0, width, 40):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, height))
    for y in range(0, height, 40):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (width, y))

def draw_boxes(screen, width, height):
    """
    This draws the individual boxes
    It also appends the individual boxes from top to bottom going towards the right
    """
    
    for i in range(rows):
        for j in range(columns):
            pygame.draw.rect(screen, (0, 255, 0), (i * 40, j * 40, 40, 40))
            boxes.append((screen, [0, 255, 0], (i * 40, j * 40, 40, 40)))
    return boxes

def hand_draw(screen, width, height):
    """
    This changes the color of the clicked box to red
    """
    
    for box in boxes:
        if box[1] == [255, 0, 0]:
            pygame.draw.rect(screen, (255, 0, 0), box[2])

while active:
    
    cursor = pygame.mouse.get_pos()
    
    if drawn == False: # Stops the green boxes from drawing again
        draw_boxes(screen, width, height)
        drawn = True
        
    hand_draw(screen, width, height)
    draw_grid(screen, width, height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            char_hold = {}
            if event.key == pygame.K_SPACE:
                with open("grid.txt", "w", encoding="utf-8") as f:
                    for i, box in enumerate(boxes):

                        if i < 20: # This is basically creating the outline of the dictionary

                            if box[1] == [255, 0, 0]: # If the box is red, then we will add it to the dictionary as an " ▢ "
                                char_hold[i] = "▢"
                            else:
                                char_hold[i] = "▥"  # If the box is green, then we will add it to the dictionary as an " ▥ "
                        else:
                            if counter == 20:  # This is resetting the counter so then values over 20 can be added to the dictionary
                                counter = 0

                            if box[1] == [255, 0, 0]: # This is now adding to the dictionary instead of setting it
                                char_hold[counter] += "▢"
                            else:
                                char_hold[counter] += "▥"

                            counter += 1

                    for i in char_hold:
                        f.write((char_hold[i]) + "\n") # prints each key on separate lines.

        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if pygame.Rect(box[2]).collidepoint(cursor): # box[2] are the coordinates of the box
                    box[1][0] = 255 # turns the green box into red
                    box[1][1] = 0 # Removes the green value

    pygame.display.update()
