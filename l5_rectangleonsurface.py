# Importing the library
import pygame
# import time

# Initializing Pygame
pygame.init()

# Creating the window
window = pygame.display.set_mode((400,300))

# Choosing a color for the rectangle
color = (255,255,0) #yellow

# Drawing Rectangle
pygame.draw.rect(window, color, pygame.Rect(30, 30, 60, 60))


# The pygame.display.flip() method is used to update content on the display screen
pygame.display.flip()

# Creating a bool value which checks if game is running
running = True

# Keep game running till running is true
while running:
	
	# Check for event if user has pushed
	# any event in queue
	for event in pygame.event.get():
		
		# If event is of type quit then set
		# running bool to false
		if event.type == pygame.QUIT:
			running = False