# Importing pygame module
import asyncio
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# COUNT_DOWN = 3

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# creating list in which we will store
# the position of the circle
circle_positions = []

# radius of the circle
circle_radius = 60

# Color of the circle
color = (0, 0, 255)

# Creating a variable which we will use
# to run the while loop
run = True

async def main():
    
	while True:
		
		# global COUNT_DOWN
		# COUNT_DOWN = 3
	# Iterating over all the events received from
	# pygame.event.get()
		for event in pygame.event.get():

		# If the type of the event is quit
		# then setting the run variable to false
			if event.type == QUIT:
				# run = False
				pygame.quit()

			# quit the program.
				quit()


		# if the type of the event is MOUSEBUTTONDOWN
		# then storing the current position
			elif event.type == MOUSEBUTTONDOWN:
				position = event.pos
				circle_positions.append(position)
			
	# Using for loop to iterate
	# over the circle_positions
	# list
		for position in circle_positions:

		# Drawing the circle
			pygame.draw.circle(window, color, position,
							circle_radius)

	# Draws the surface object to the screen.
		
		# print(f""" Hello[{COUNT_DOWN}] from Python""")
		await asyncio.sleep(0)  # Very important, and keep it 0
		
		# if not COUNT_DOWN:
			# return
		
		# COUNT_DOWN = COUNT_DOWN - 1
		pygame.display.update()

asyncio.run(main())



