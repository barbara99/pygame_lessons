# Importing the library
import pygame
 
# Initializing Pygame
pygame.init()
 
# Initializing surface
window = pygame.display.set_mode((400, 300))
 
# Initializing RGB Color
red = (255, 0, 0) # red
blue = (0, 0, 255) # blue
 
# Changing window color
window.fill(blue)
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