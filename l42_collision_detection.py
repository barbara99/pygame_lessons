# part 1

# import required libraries
import pygame
import random

# initialize pygame objects
pygame.init()

# define the colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# set the Dimensions
width = 650
height = 700

# size of a block
pixel = 64

# set Screen
screen = pygame.display.set_mode((width,
								height))

# set caption
pygame.display.set_caption("CORONA SCARPER")

# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)

# load the image
gameIcon = pygame.image.load("sm.png")

# Scale the image to your needed size
gameIcon = pygame.transform.scale(gameIcon, DEFAULT_IMAGE_SIZE)

# Set a default position
DEFAULT_IMAGE_POSITION = (200,200)


# set icon
pygame.display.set_icon(gameIcon)

# load the image
backgroundImg = pygame.image.load("bacgrd.jpg")

# part 2
# load the image
playerImage = pygame.image.load("sample_logo.png")
# Scale the image to your needed size
playerImage = pygame.transform.scale(playerImage, DEFAULT_IMAGE_SIZE)


# set the position
playerXPosition = (width/2) - (pixel/2)

# So that the player will be
# at height of 20 above the base
playerYPosition = height - pixel - 10	

# set initially 0
playerXPositionChange = 0

# define a function for setting
# the image at particular
# coordinates
def player(x, y):
# paste image on screen object
    screen.blit(playerImage, (x, y))
    pygame.display.flip()


# load the image
blockImage = pygame.image.load("sm.png")

# Scale the image to your needed size
blockImage = pygame.transform.scale(gameIcon, DEFAULT_IMAGE_SIZE)
# set the random position
blockXPosition = random.randint(0,
								(width - pixel))

blockYPosition = 0 - pixel

# set the speed of
# the block
blockXPositionChange = 0
blockYPositionChange = 2

# define a function for setting
# the image at particular
# coordinates
def block(x, y):
# paste image on screen object
    screen.blit(blockImage,(x, y))
    pygame.display.update()



# part 3

# define a function for
# collision detection
def crash():
# take a global variable
    global blockYPosition

# check conditions
    if playerYPosition < (blockYPosition + pixel):

	    if ((playerXPosition > blockXPosition
		    and playerXPosition < (blockXPosition + pixel))
		    or ((playerXPosition + pixel) > blockXPosition
		    and (playerXPosition + pixel) < (blockXPosition + pixel))):

		    blockYPosition = height + 1000

# part 4

running = True

while running:
# set the image on screen object
    screen.blit(backgroundImg, (0, 0))
    pygame.display.flip()

    # loop through all events
    for event in pygame.event.get():
		
	# check the quit condition
	    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerXPositionChange = 3

		    
            

            if event.key == pygame.K_LEFT:
                playerXPositionChange = -3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                playerXPositionChange = 0
        if event.type == pygame.QUIT:
                pygame.quit()

# part 5

# Boundaries to the Player

# if it comes at right end,
# stay at right end and
# does not exceed
if playerXPosition >= (width - pixel):
    playerXPosition = (width - pixel)

# if it comes at left end,
# stay at left end and
# does not exceed
if playerXPosition <= 0:
    playerXPosition = 0


# part 6

# Multiple Blocks Movement after each other
# and condition used because of game over function
if (blockYPosition >= height - 0 and
	blockYPosition <= (height + 200)):

    blockYPosition = 0 - pixel

# randomly assign value in range
    blockXPosition = random.randint(0, (width - pixel))


# movement of Player
    playerXPosition += playerXPositionChange

# movement of Block
    blockYPosition += blockYPositionChange

# player Function Call
    player(playerXPosition, playerYPosition)

# block Function Call
    block(blockXPosition, blockYPosition)

# crash function call
    crash()

# update screen
    pygame.display.update()
