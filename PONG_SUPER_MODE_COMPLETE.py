#KPL Intro to Coding Final Project
#The Pong code is started but not complete
#Pong in progress - Starting point for class # 7

# Import Modules and Declare Global Variables

import random, sys, time, pygame
from pygame.locals import *


pygame.init() # starts pygame

FPS = 60 # 60 Frames per second
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1280
ball_HEIGHT = 25
ball_WIDTH = 25
ball_SPEED = 5

ball_x_speed = ball_SPEED
ball_y_speed = ball_SPEED
score1 = 0 # This is the score for player 1
score2 = 0 # This is the score for player 2


# Set up colors for future use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Starting position of the Ball
ball_x_pos = SCREEN_WIDTH//2
ball_y_pos = SCREEN_HEIGHT//2


# Load the graphics
#theballGraphic = pygame.image.load('pong_ball_25_cube.png') 
#right_paddle = pygame.image.load('pong_paddle.png')
#left_paddle = pygame.image.load('pong_paddle.png')
background_image = pygame.image.load('backsplash2.png') # Load the background image file

# Set up the Game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Pong in Progress") #This is the title


#Load the Sound effects
pygame.mixer.init(44100, -16, 2, 2048)
#beep1 = pygame.mixer.Sound('pongBlip1.ogg')
#beep2 = pygame.mixer.Sound('pongBlip2.ogg')


#mouseX, mouseY = pygame.mouse.
'''
class ButtonGenerator:
    def __init__(self):
        self.rect = pygame.draw.rect(DISPLAYSURF, (255,0,0,), (100,100,200,300))
'''

class ButtonGenerator():
    def __init__(self):
        self.image = pygame.image.load("200_118_DVD_Logo_B.png")
        self.rect = pygame.draw.rect(DISPLAYSURF, (0,255,0),(400, 200, 450, 100))

#buttonImage = pygame.image.load("200_118_DVD_Logo_B.png")
#buttonRect = buttonImage.get_rect()

# Helper functions


#logoRect = logo1.image.get_rect()

def scoreBoard():
    RETROFONT = pygame.font.Font('PressStart2P.ttf', 48)
    scoreSurf = RETROFONT.render("Test", True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (SCREEN_WIDTH//3, SCREEN_HEIGHT //5)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


# The Main "game" loop

def main():
    global FPSCLOCK

    DISPLAYSURF.fill(BLACK) # Paint the whole screen a certain color
    DISPLAYSURF.blit(background_image, (0,0)) #Blit the background image to the Display Surface
    pygame.draw.line(DISPLAYSURF, BLUE, (SCREEN_WIDTH//2,0),(SCREEN_WIDTH//2,SCREEN_HEIGHT),25)
    logo1 = ButtonGenerator()
    scoreBoard() # Run the scoreboard function
    #DISPLAYSURF.blit(logo1.image, (400,400))
    pygame.display.update()    # Refreshes the display
    fpsClock.tick(FPS)\


    # Check for a QUIT event (such as closing the window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                print("player 2 pressed up")
                Paddle2_up = True
                Paddle2_down = False
            if event.key == K_DOWN:
                print("player 2 pressed down")
                Paddle2_up = False
                Paddle2_down = True
            if event.key == K_w:
                print("player 1 pressed up")
                Paddle1_up = True
                Paddle1_down = False
                pygame.quit()
                sys.exit()
            if event.key == K_s:
                print("player 1 pressed down")
                Paddle1_up = False
                Paddle1_down = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if player.rect.collidepoint(pygame.mouse.get_pos()):
            if logo1.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicke on the player")
                pygame.quit()
                sys.exit()
    
while True:
    main()
