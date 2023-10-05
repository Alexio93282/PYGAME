import pygame as pg

import random

pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0)
YELLOW = (255,255,0)
BLUE = (0,0,255)

screen = pg.display.set_mode((1280,1024))

clock = pg.time.Clock()

pos_x =580
pos_y = 450

size_x = 100
size_y = 100


i = 0
playing = True
while playing:
    clock.tick(120)
    print("Jackpot", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
    
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pos_y -= 5
    if keys[pg.K_s]:
        pos_y += 5
    if keys[pg.K_a]:
        pos_x -= 5
    if keys[pg.K_d]:
        pos_x += 5

    if pos_x > 1200:
        pos_x = 1200

    screen.fill(BLUE)

    player_box = pg.Rect(pos_x,pos_y, size_x,size_y)
    pg.draw.rect(screen, RED, player_box)
    size_x += random.randint(-10,10)
    size_y += random.randint(-10,10)
    
    pg.display.update()

    #pos_x += 10
    #if pos_x > 1200:
       # pos_x = -200
       # pos_y += 10