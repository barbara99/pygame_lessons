# import pygame module
import pygame

# initializing imported module
pygame.init()

# Displaying a window of height 500 and width 400
pygame.display.set_mode((400, 500))

# Here we set name or title of our pygame window
pygame.display.set_caption('IIPGH')

# Here we load the image we want to use
Icon = pygame.image.load('sample_logo.png')

# We use set_icon to set new icon
pygame.display.set_icon(Icon)

# Creating a bool value which checks if game is running
running = True

# Keep game running till running is true
while running:
	
	# Check for event if user has pushed any event in queue
	for event in pygame.event.get():
		
		# If event is of type quit then set running bool to false
		if event.type == pygame.QUIT:
			running = False
