# more info on https://www.geeksforgeeks.org/pygame-surface/

# Importing the library
import pygame


# Initializing Pygame
pygame.init()

# creating the display surface
# display_surface = pygame.display.set_mode((700, 800 ))
window = pygame.display.set_mode((300, 400))
color = "red"

# Creating the image surface
image = pygame.image.load('bg.jpg')

# putting our image surface on display surface
window.blit(image,(60,60))
pygame.draw.rect(window, color, pygame.Rect(30, 30, 60, 60))

# updating the display
pygame.display.flip()

# Creating a bool value which checks if game is running
running = True

# Keep game running till running is true
while running:
	
	# Check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		# If event is of type quit then set running bool to false
		if event.type == pygame.QUIT:
			running = False