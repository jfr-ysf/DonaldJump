import pygame as pg
import random
import sys

pg.init()
WIDTH = 1000
HEIGHT = 768
width = 71
height = 60
speed = 30
FPS = 30
x = 60
y = 550
x1=60
y1=550

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pl = pg.image.load('idle.png').convert_alpha()
pl.set_colorkey(WHITE)
bg = pg.image.load('bg1.jpg').convert_alpha()
pg.display.set_caption("Don Trump")
clock = pg.time.Clock()
left = False
right = False
animaCount = 0
last_move = "right"
jump = False
jumpCount = 10
v = 5
m = 1
ball=pg.image.load('ball.png').convert_alpha()
r1=pg.image.load('right_1.png').convert_alpha()
r2=pg.image.load('right_2.png').convert_alpha()
r3=pg.image.load('right_3.png').convert_alpha()
r4=pg.image.load('right_4.png').convert_alpha()
r5=pg.image.load('right_5.png').convert_alpha()
r6=pg.image.load('right_6.png').convert_alpha()
l1=pg.image.load('left_1.png').convert_alpha()
l2=pg.image.load('left_1.png').convert_alpha()
l3=pg.image.load('left_1.png').convert_alpha()
l4=pg.image.load('left_1.png').convert_alpha()
l5=pg.image.load('left_1.png').convert_alpha()
l6=pg.image.load('left_1.png').convert_alpha()
ball.set_colorkey(WHITE)
r1.set_colorkey(WHITE)
r2.set_colorkey(WHITE)
r3.set_colorkey(WHITE)
r4.set_colorkey(WHITE)
r5.set_colorkey(WHITE)
r6.set_colorkey(WHITE)
l1.set_colorkey(WHITE)
l2.set_colorkey(WHITE)
l3.set_colorkey(WHITE)
l4.set_colorkey(WHITE)
l5.set_colorkey(WHITE)
l6.set_colorkey(WHITE)

walkRight = [r1,r2,r3,r4,r5,r6]
walkLeft = [l1,l2,l3,l4,l5,l6]

def drawWindow():
    global animaCount
    screen.blit(bg, (0, 0))

    if animaCount + 1 >= 30:
        animaCount = 0

    if left:
        screen.blit(walkLeft[animaCount // 6], (x, y))
        animaCount += 1
    elif right:
        screen.blit(walkRight[animaCount // 6], (x, y))
        animaCount += 1
    else:
        screen.blit(pl, (x, y))

running = True
while running:
    clock.tick(FPS)
    screen.blit(pl, (x, y))
    screen.blit(ball, (x1,y1))
    screen.blit(bg, (0, 0))
    


    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
            sys.exit()

    key = pg.key.get_pressed()
    if key[pg.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif key[pg.K_RIGHT] and x < WIDTH - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animaCount = 0
    if not jump:
        if key[pg.K_SPACE]:
            jump = True
    if jump:
        F = (1 / 2) * m * (v ** 2)
        y -= F
        v = v - 1
        if v < 0:
            m = -1
        if v == -6:
            jump = False
            v = 7.5
            m = 1

    drawWindow()
    pg.display.update()
