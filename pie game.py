import pygame as pg
from Characters import *
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


all_sprites = pg.sprite.Group()
player = Player(all_sprites)
enemy = Enemy()
all_sprites.add(player)
all_sprites.add(enemy)
enemies = pg.sprite.Group()
enemies.add(enemy)


pos_x =580
pos_y = 450
size_x = 50
size_y = 50
box_1_dir = 5

size_x = 100
size_y = 100

pos_x2 = 600
pos_y2 = 100
size_x2 = 50
size_y2 = 50
box_2_dir = -5


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


    if len(all_sprites) < 10:
        new_enemy = Enemy()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)

    all_sprites.update()
    
    HJONK_HJONK = pg.sprite.spritecollide(player, enemies, True )
    if HJONK_HJONK:
        print("I am up one, Where did you learn to count we are even")

    screen.fill(BLUE)
    all_sprites.draw(screen)

    pg.display.update()

    #pos_x += 10
    #if pos_x > 1200:
       # pos_x = -200
       # pos_y += 10