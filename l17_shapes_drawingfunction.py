# Importing pygame module
import pygame
from pygame.locals import *

# Creating Drawing function


def drawingfunction(x, y, width, height):

	# Creating rectangle using the draw.rect() method
	pygame.draw.rect(window, (0, 0, 255), [x, y, width, height])

	# Calculation the center of the circle
	circle_x = width/2 + x
	circle_y = height/2 + y

	# Calculating the radius of the circle
	if height < width:
		radius = height/2
	else:
		radius = width/2

	# Drawing the circle
	pygame.draw.circle(window, (0, 255, 0), [circle_x, circle_y], radius)


# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Calling the drawing function
drawingfunction(50, 200, 550, 400)

# Draws the surface object to the screen.
pygame.display.update()

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