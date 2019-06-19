#!/usr/bin/env python3
 
#
# Adapted by Matthew Billman from pygame (simple) template - by furas
#
# https://github.com/furas/my-python-codes/tree/master/pygame/__template__/
#
 
# ---------------------------------------------------------------------
 
__author__  = 'Bartlomiej "furas" Burek'
__webpage__ = 'http://blog.furas.pl'
 
# ---------------------------------------------------------------------
 
import pygame
import math
from pygame.image import load_basic

# === CONSTANTS === (UPPER_CASE names)
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
 
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
 
SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 400
 
BLOCK_SIZE = 50
 
# === CLASSES === (CamelCase names)
 
'''
class Button():
'''
   
# === FUNCTIONS === (lower_case names)
 
    # empty
   
# === MAIN === (lower_case names)
 
# --- (global) variables ---
 
# --- init ---
 
pygame.init()
 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()
 
# --- objects ---
 
'''
button = Button(...)
'''

class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/ball.jpeg')
        self.rect = pygame.Rect((50,50,50,50))
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
 
rects = []

w_padding = SCREEN_WIDTH/BLOCK_SIZE
h_padding = (SCREEN_HEIGHT/2)-(BLOCK_SIZE/2)

#Will appear on the left:
rects.append(pygame.Rect(w_padding, h_padding, BLOCK_SIZE, BLOCK_SIZE))
#Will appear on the right:
rects.append(pygame.Rect(SCREEN_WIDTH-(w_padding+BLOCK_SIZE), h_padding, BLOCK_SIZE, BLOCK_SIZE))

ball = Ball((20,5))
 
selected = None
   
# --- mainloop ---
 
clock = pygame.time.Clock()
is_running = True
 
while is_running:
 
    # --- events ---
   
    for event in pygame.event.get():
 
        # --- global events ---
       
        if event.type == pygame.QUIT:
            is_running = False
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False
 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, r in enumerate(rects):
                    if r.collidepoint(event.pos):
                        selected = i
                        selected_offset_x = r.x - event.pos[0]
                        selected_offset_y = r.y - event.pos[1]
               
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected = None
               
        elif event.type == pygame.MOUSEMOTION:
            if selected is not None: # selected can be `0` so `is not None` is required
                # move object
                rects[selected].x = event.pos[0] + selected_offset_x
                rects[selected].y = event.pos[1] + selected_offset_y
               
        # --- objects events ---
 
        '''
       button.handle_event(event)
       '''
       
    # --- updates ---

    ball.update()
    print('Ball moved to {}').format(ball)
       
    # --- draws ---
   
    screen.fill(BLACK)
 
    '''
    button.draw(screen)    
    '''
   
    # draw rect
    for r in rects:
        pygame.draw.rect(screen, RED, r)
       
    pygame.display.update()
 
    # --- FPS ---
 
    clock.tick(60)
 
# --- the end ---
   
pygame.quit()
