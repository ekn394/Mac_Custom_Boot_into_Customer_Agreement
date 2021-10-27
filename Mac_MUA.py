#KPL Intro to Coding Final Project
#The Pong code is started but not complete
#Pong in progress - Starting point for class # 7

# Import Modules and Declare Global Variables

import random, sys, time, pygame
from pygame.locals import *

pygame.init() # starts pygame

FPS = 60 # 60 Frames per second
fpsClock = pygame.time.Clock()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Set up colors for future use
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load the Graphics
background_image = pygame.image.load('backsplash_1200_899.png') # Load the background image file

# Set up the Game window
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("KPL Mac Computer Use Message") #This is the title

class ButtonGenerator():
    def __init__(self):
        self.rect = pygame.draw.rect(DISPLAYSURF, (0,0,200),(500, 700, 300, 100), 0, border_radius=15)

def messageText():
    KPL_FONT_TITLE = pygame.font.Font('LSANSD.TTF', 24)
    KPL_FONT_REG = pygame.font.Font('LSANS.TTF', 18)
    TITLE_Surf = KPL_FONT_TITLE.render("Computer Use Policy", True, BLACK, WHITE)
    TITLE_Rect = TITLE_Surf.get_rect()
    TITLE_Rect.centerx = DISPLAYSURF.get_rect().centerx
    TITLE_Rect.centery = 150
    BORDER_Rect = pygame.draw.rect(DISPLAYSURF, (255,255,255), (TITLE_Rect.left - 200, TITLE_Rect.top - 50, TITLE_Rect.width + 400, TITLE_Rect.height + 400), 0, border_radius = 10)
    DISPLAYSURF.blit(TITLE_Surf, TITLE_Rect)

    MSG_Surf1 = KPL_FONT_REG.render("I agree to comply with the KPL's Safe Use Code & Internet Access Policy. ", True, BLACK, WHITE)
    MSG_Rect1 = MSG_Surf1.get_rect()
    MSG_Rect1.centerx = DISPLAYSURF.get_rect().centerx
    MSG_Rect1.centery = 250
    DISPLAYSURF.blit(MSG_Surf1, MSG_Rect1)

    MSG_Surf2 = KPL_FONT_REG.render("I understand that the computers may be used for lawful puposes only.", True, BLACK, WHITE)
    MSG_Rect2 = MSG_Surf2.get_rect()
    MSG_Rect2.centerx = DISPLAYSURF.get_rect().centerx
    MSG_Rect2.centery = 290
    DISPLAYSURF.blit(MSG_Surf2, MSG_Rect2)

'''
    MSG_Surf3 = KPL_FONT_REG.render("Wake up, Neo.", True, BLACK, WHITE)
    MSG_Rect3 = MSG_Surf3.get_rect()
    MSG_Rect3.centerx = DISPLAYSURF.get_rect().centerx
    MSG_Rect3.centery = 330
    DISPLAYSURF.blit(MSG_Surf3, MSG_Rect3)
'''
# Helper functions

def buttonText():
    KPL_FONT_BOLD = pygame.font.Font('LSANSD.TTF', 48)
    ACCEPT_Surf = KPL_FONT_BOLD.render(" Accept", True, WHITE, )
    ACCEPT_Rect = ACCEPT_Surf.get_rect()
    ACCEPT_Rect.topleft = (550, 715)
    DISPLAYSURF.blit(ACCEPT_Surf, ACCEPT_Rect)

# The Main "game" loop

def main():
    global FPSCLOCK

    DISPLAYSURF.fill(BLACK) # Paint the whole screen a certain color
    DISPLAYSURF.blit(background_image, (40,0)) #Blit the background image to the Display Surface
    button = ButtonGenerator() # Draw the blue button
    message = messageText()
    buttonText() # Draw the Text on the Button
    pygame.display.update()    # Refreshes the display
    fpsClock.tick(FPS)\

    # Check for a QUIT event (such as closing the window)
    for event in pygame.event.get():
        '''
        if event.type == QUIT:
            #pygame.quit()
            #sys.exit()
            #print("This was disabled to make Command Q stop being an escape hatch")
        
        if event.type == KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_k] and pressed_keys[K_p] and pressed_keys[K_l]:
                print("New escape hatch!")
                pygame.quit()
                sys.exit()
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if player.rect.collidepoint(pygame.mouse.get_pos()):
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                print("Mouse clicked on the Accept button")
                pygame.quit()
                sys.exit()
    
while True:
    main()
