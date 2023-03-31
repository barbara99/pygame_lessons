# https://www.geeksforgeeks.org/how-to-draw-a-rectangle-with-rounded-corner-in-pygame/

# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initializing Color
color = (48, 141, 70)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60), 1, 9)
pygame.display.flip()

# creating a bool value which checks
# if game is running
running = True
  
# keep game running till running is true
while running:
      
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
          
        # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False