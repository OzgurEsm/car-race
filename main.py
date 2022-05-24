import pygame
from pygame.locals import * 
import random

size = width, height = (800,800) ;"""in order to get relative coordinates
work or change size later we can assign screen size like this.Tuple btw"""
road_width = int(width/1.6) ;""" 500 in this case and change to int"""
roadmark_width = int(width/80) ;"""Doing math on our own here"""
right_lane = width/2 + road_width/4 
left_lane = width/2 - road_width/4 ;"""we made these x-axis coords to ease reading"""
speed = 3

pygame.init()
running = True ;""" instead of a func  we chose a var i guess """
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pygame P1 Racing') ;"""Title,just learned to use semi-colon like this"""
screen.fill((200,150,250)) ;"""background rgb in tuple,i like purple"""

pygame.display.update() ;"""updates our changes to display"""

my_car = pygame.image.load("car-race\car1.png") ; """loaded image of our car"""
my_car_loc = my_car.get_rect() ;"""location of our car"""
my_car_loc.center =  right_lane, height*0.8 ;"""x,y coord for center of our car"""
other_car = pygame.image.load('car-race\car2.png')
other_car_loc = other_car.get_rect()
other_car_loc.center = left_lane, height*0.2

counter = 0
while running:
    counter += 1
    if counter == 2000:
        speed += 2
        counter = 0
        print(f'Next Level,your current speed: {speed}')
    # other car animation
    other_car_loc[1] += speed  
    """from [x,y] chose y coord and created movement by adding to y axis"""
    if other_car_loc[1] > height:
        """other_car_loc[1] =  -200 # re-entering from -200 # removed this lane since we mentioned y-axis down"""
        if random.randint(0,1) == 0: 
            other_car_loc.center = right_lane, -200 
        else:
            other_car_loc.center = left_lane, -200 ;"""randomly choosing lanes here, dont forget .center"""
    
    #Fail condition
    if my_car_loc[0] == other_car_loc[0] and other_car_loc[1] > my_car_loc[1] - 250:
        break
    """ if x coords equal and other_car height greater than my_car minus pixelheight:250 they crash"""
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN: #pressing key #stopped my_car going of screen by cheking it's lane
            if event.key in [K_a, K_LEFT] and my_car_loc.center[0]== right_lane: #pressing a or left arrow while my_car is on right_lane
                my_car_loc = my_car_loc.move([-road_width/2, 0]) # new coords in list
            if event.key in [K_d, K_RIGHT] and my_car_loc.center[0]== left_lane:
                my_car_loc = my_car_loc.move([road_width/2, 0])
            if event.key in [K_w, K_UP]:
                speed += 1
                print(f'Your new speed is: {speed}')
    pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2 - road_width/2, 0, road_width, height) 
    ) ; """(x,y,width,height) in tuple centered rectangle coord."""

    pygame.draw.rect(
    screen,
    (255,255,0),
    (width/2 - roadmark_width/2, 0, roadmark_width,height)
    ) ; """Yellow line right in the middle"""

    pygame.draw.rect(
    screen,
    (250,250,250),
    (width/2 - road_width/2 + roadmark_width*2, 0, roadmark_width,height)
    ) ;""" draw left white line """

    pygame.draw.rect(
    screen,
    (250,250,250),
    (width/2 + road_width/2 -roadmark_width*3, 0, roadmark_width,height)
    ) ;"""draw right white line,used relative coordinates all along the way!"""
        
    screen.blit(my_car, my_car_loc) ;"""draw image,location"""
    screen.blit(other_car,other_car_loc)
    pygame.display.update() ;"""need to update here"""
    
    
pygame.quit()