import pygame
import numpy as np
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load("assets/star_space.jpg").convert()

#--------VARIABLES-----------
pygame.display.set_caption('SPACE!!!!!!!')
x = 50
y = 50
w = 40
h = 60
vel = [0, 0]
dv = .5
dampner = 0.9
font = pygame.font.Font('freesansbold.ttf', 32)

points_tracker = 0

white_holex = int(SCREEN_WIDTH/2)
white_holey = int(SCREEN_HEIGHT/2)
player = pygame.Rect((x, y, w, h))
run = True
frames = 0
while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        vel[0] -= dv
    if keys[pygame.K_RIGHT]:
        vel[0] += dv
    if keys[pygame.K_UP]:
        vel[1] -= dv
    if keys[pygame.K_DOWN]:
        vel[1] += dv
    if keys[pygame.K_b]:
        vel=[v*dampner for v in vel]

    player.x += vel[0]
    player.y += vel[1]


    if player.x < 0 or player.x > SCREEN_WIDTH-w:
        vel[0] = -1*vel[0]
    if player.y <0 or player.y > SCREEN_HEIGHT-h:
        vel[1] = -1*vel[1]

    pygame.draw.rect(win, (255, 0, 0), player)
    white_hole = pygame.draw.circle(win, (255, 255, 255), (white_holex, white_holey), 72)
    if player.colliderect(white_hole):
        points_tracker += 1
        white_holex = np.random.randint(0, SCREEN_WIDTH)
        white_holey = np.random.randint(0, SCREEN_HEIGHT)

    text = font.render(f'POINTS: {points_tracker}', True, (0, 255, 43), (255, 100, 100))
    text_Rect = text.get_rect()
    win.blit(text, text_Rect)
    pygame.display.update()

    if not keys[pygame.K_f]:
        win.fill([0, 0, 0])

pygame.quit()
