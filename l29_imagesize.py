# import pygame
import pygame

# creating image object
image = pygame.image.load('bg.jpg')

# get_height method return the height of the surface pixel,
# in our case surface is image
print("Height of image= " + str(image.get_height()))

# get_width method return the width of the surface pixel,
# in our case surface is image
print("Width of image= " + str(image.get_width()))
