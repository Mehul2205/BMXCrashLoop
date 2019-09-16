# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:42:22 2019

@author: Mehul Patni
"""

import pygame
import random

pygame.init()               # initialize all imported pygame modules

# Create a new Sound object from a file or buffer object
crash_sound = pygame.mixer.Sound("Smash.wav")
start_sound = pygame.mixer.Sound("Start.wav")
pygame.mixer.music.load("Game.wav")

# Initialise the Width and Height of the screen
display_width = 800
display_height = 600

# Initialise some color with RGB configration
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


carImg = pygame.image.load('racecar.png')   # load new image from a file
car_width = 73                              # Width of that image is 73

# Initialize a window or screen for display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('BMX Crash Loop')    #Set the current window caption

clock = pygame.time.Clock()             # create an object to help track time

paused = True

# This function is used to create 4 different kind of obstacles
def load_images():   
    images = {}
    numbers = ["fire1", "stop1","stop2","tree1"]
    for i,num in enumerate(numbers, start=1):
        images[i] = pygame.image.load("{}.jpg".format(num)).convert()
        images[i] = pygame.transform.scale(images[i], (100, 100))
    return images

# To write text on the screen
def text_objects(text,font):
    textSurface = font.render(text,True,black)  # draw text on a new Surface
    return textSurface, textSurface.get_rect()  
    #textSurface.get_rect() - get the rectangular area of the Surface

# To print how many obstacles you have dodged
def  things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))        # draw one image onto another

# To select one of the images from the bunch of image the obstacles    
def things(thingx, thingy):
    object_image = load_images()        # It cantain all kind of obstacles
    object1 = random.randint(1,4)       #Return random integers
    gameDisplay.blit(object_image[object1],(thingx, thingy)) # draw one image onto another
    
# To display car.
def car(x,y):
    gameDisplay.blit(carImg,(x,y))      # draw one image onto another

# This is executed when car crashes with an obstacle
def crash():
    pygame.mixer.music.stop()               # stop the music playback
    pygame.mixer.Sound.play(crash_sound)    # begin sound playback
    game_Exit()                             # To Display the last screen

# To Quit pygame screen
def QUit():
    pygame.quit()
    quit()

# To Display button on the screen
def BUTTON(message,x_coordinate,y_coordinate,width,height,inactivecolor,activecolor,action = None):
    
    mouse = pygame.mouse.get_pos()          # get the mouse cursor position
    click = pygame.mouse.get_pressed()      # get the state of the mouse buttons
    
    # To check if mouse is over the button or not i.e, hover feature of button
    if x_coordinate+width > mouse[0] > x_coordinate  and y_coordinate+height > mouse[1] > y_coordinate :
        pygame.draw.rect(gameDisplay,activecolor,(x_coordinate,y_coordinate,width,height)) # Draw rectangle on screen
        if click[0] == 1 and action != None :
            action()
    else:    
        pygame.draw.rect(gameDisplay,inactivecolor,(x_coordinate,y_coordinate,width,height)) # Draw rectangle on screen
        
    smallText = pygame.font.Font('PressStart2P-Regular.ttf',15)
    textSurf, textRect = text_objects(message, smallText)   # draw text on a new Surface
    textRect.center = ((x_coordinate+width/2), (y_coordinate+height/2))
    gameDisplay.blit(textSurf,textRect)     # draw one image onto another

# To unpause screen when user clicks continue
def unpaused():

    global pause
    pause = False           
    pygame.mixer.music.unpause()        # resume paused music

# This function is called when player pauses the game.
def paused():

    pygame.mixer.music.pause()          # temporarily stop music playback
    global pause
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         
        # To display the pause screen 
        gameDisplay.fill(white)
        largeText = pygame.font.Font('PressStart2P-Regular.ttf',65)
        TextSurf, TextRect = text_objects("Paused",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)      # draw one image onto another
        BUTTON("Continue",150,450,150,50,green,bright_green,unpaused)        
        BUTTON("QUIT!",550,450,150,50,red,bright_red,QUit)        
        pygame.display.update()
        clock.tick(15)

# This function is called when player crashes.
def game_Exit():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # To check if user presses X(exit) button
                pygame.quit()
                quit()
        
        # To display the screen when chrashes
        gameDisplay.fill(white)
        largeText = pygame.font.Font('PressStart2P-Regular.ttf',50)
        TextSurf, TextRect = text_objects("You Crashed!",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)    # draw one image onto another
        BUTTON("Play Again?",150,450,200,50,green,bright_green,game_loop)        
        BUTTON("QUIT!",550,450,200,50,red,bright_red,QUit)        
        pygame.display.update() # Update portions of the screen for software displays
        clock.tick(15)
                       
#
def game_intro():
    
    pygame.mixer.Sound.play(start_sound,loops =-1)
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # To check if user presses X(exit) button
                pygame.quit()
                quit()
    
        # To display the screen when game starts
        gameDisplay.fill(white)
        largeText = pygame.font.Font('PressStart2P-Regular.ttf',50)
        TextSurf, TextRect = text_objects("BMX Crash Loop",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)    # draw one image onto another
        BUTTON("GO!",150,450,100,50,green,bright_green,game_loop)        
        BUTTON("QUIT!",550,450,100,50,red,bright_red,QUit)        
        pygame.display.update() # Update portions of the screen for software displays
        clock.tick(15)


def game_loop():
    pygame.mixer.music.play(-1)             # Start the playback of the music stream
    pygame.mixer.Sound.stop(start_sound)    # stop sound playback
    pygame.mixer.Sound.stop(crash_sound)    # stop sound playback
    global pause
    
    # These are the x and y co-ordinates of car 
    x= (display_width*.45)
    y = (display_height*.8)
    x_change = 0

    thing_startx = random.randrange(0,display_width-100)    # To bring obstacle randomly on the screen
    thing_starty = -100                                     # Start Object with no display
    thing_speed = 7                                         # Speed of the object
    thing_width = 100;                                      # Width of the object
    thing_height = 100                                      # Height of the object

    dodged = 0
    
    # Load first obstacle
    object_image = load_images()
    object1 = random.randint(1,4)
    
    # These are the dimension of second object.
    thing_startx1 = random.randrange(0,display_width-100)
    thing_starty1 = -400
    object2 = random.randint(1,4)
    
    # And from here the actual game starts, This is the loop where we handle all kind of events.
    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # To check if user presses X(exit) button
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:        # Check if any key is pressed
                if event.key == pygame.K_LEFT:      # Check if the pressed key is left arrow
                    x_change = -10
                elif event.key == pygame.K_RIGHT:   # Check if the key pressed is right arrow
                    x_change = 10
                elif event.key == pygame.K_p:       # Check if player presses p to pause the game
                    pause = True
                    paused()
        
            if event.type == pygame.KEYUP:          # Check if user lift his finger from the key
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   # Check for left or right arrow
                    x_change = 0;
                    
        x += x_change;                              # modify x co-ordinate of the car
        gameDisplay.fill(white)                     # fill Surface with a solid color
        car(x,y)                                    # To display car
        things_dodged(dodged)                        # To display dodged count

        # To check if object1 has exit the screen or not 
            # if yes then start that object again from the top        
        if(thing_starty >= display_height):
            thing_startx = random.randrange(0,display_width-100)
            thing_starty = -100
            object1 = random.randint(1,4)       # To select random object
            dodged +=1
            if dodged % 5 == 0:
                thing_speed +=1
        
        # if dodged is greater than 10 then object2 comes into the picture
        if dodged >= 10:
            thing_starty1 += thing_speed
            gameDisplay.blit(object_image[object2],(thing_startx1, thing_starty1)) # draw one image onto another


        # To check if object2 has exit the screen or not 
            # if yes then start that object again from the top
        if(thing_starty1 >= display_height):
            thing_startx1 = random.randrange(0,display_width-100)
            thing_starty1 = -100
            object2 = random.randint(1,4)       # To select random object
            dodged +=1

        # These next two lines is to display and move object1
        gameDisplay.blit(object_image[object1],(thing_startx, thing_starty))        # draw one image onto another
        thing_starty += thing_speed
        
        # Check if object1 crashes with car or not
        if y <= thing_starty+thing_height :
            if (thing_startx < x and x < thing_startx+thing_width) or (thing_startx < x+car_width and x+car_width < thing_startx+thing_width):
                crash()
        
        # Check if object2 crashes with car or not
        if y <= thing_starty1+thing_height :
            if (thing_startx1 < x and x < thing_startx1+thing_width) or (thing_startx1 < x+car_width and x+car_width < thing_startx1+thing_width):
                crash()
                
        # Make sure that car remain 
        if x> display_width-car_width  or x < 0:
            crash()
        
        pygame.display.update()         # Update portions of the screen for software displays
        clock.tick(60)      # FPS
        
game_intro()