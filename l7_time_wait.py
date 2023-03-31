# pygame.time.wait
# This function is used to pause the running of the program for few seconds. 
# it takes time in milliseconds as parameter. 
# For example to demonstrate this function we will write a simple program to make a logo appear on screen only after 5 seconds. 
# The code for this will be:

# importing pygame module
import pygame

# importing sys module
import sys

# initialising pygame
pygame.init()

# creating display
display = pygame.display.set_mode((500, 500))

# Creating the image surface
image = pygame.image.load('bg.jpg')

# putting our image surface on display surface
display.blit(image,(100,100))

# making the script wait for 5000 seconds
pygame.time.wait(7000)

pygame.display.flip()

# creating a running loop
while True:

	# creating a loop to check events that are occurring
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	# updating the display
	# pygame.display.flip()
