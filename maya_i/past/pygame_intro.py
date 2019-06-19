import sys, pygame
from pygame import time
pygame.init()

size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

t_i = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    t_i = time.get_ticks()/1000
    dampener = .9

    ballrect = ballrect.move(speed)


    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        print(speed)
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        print(speed)





    screen.fill(black)

    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 100, 50))

    screen.blit(ball, ballrect)
    pygame.display.flip()

    #GRAVITY:
    g = 9.8
    v_y_i = speed[1]
    t_f = time.get_ticks()/1000
    dt = t_f-t_i
    v_y_f = v_y_i + (g * dt)
    speed[1] = v_y_f
    t_i = t_f