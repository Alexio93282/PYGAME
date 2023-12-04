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

screen = pg.display.set_mode((2560,1440))
clock = pg.time.Clock()

font_cs30 = pg.font.SysFont("Comic Sans", 30)
font_times40 = pg.font.SysFont("Times New Roman", 40)

pg.mixer.music.load('images/BTLDMC.ogg') 
pg.mixer.music.play(-1) 

all_sprites = pg.sprite.Group()
enemies = pg.sprite.Group()
player = Player(all_sprites, enemies)
enemy = Enemy()
enemy2 = Enemy2()
all_sprites.add(player)
all_sprites.add(enemy)
enemies.add(enemy)
enemies.add(enemy2)

pos_x =580
pos_y = 450

i = 0
playing = True
while playing:
    clock.tick(30)
    print("Jackpot", i)
    i += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
    

    if pos_x > 1200:
        pos_x = 1200

    if len(enemies) < 15:
        new_enemy = Enemy()
        new_enemy2 = Enemy2()
        all_sprites.add(new_enemy)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy2)
        enemies.add(new_enemy2)

    all_sprites.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    if hits:
        #player.hp -= 10
        player.take_dmg(10)
 
        print(player.hp)
        
        hp_text = font_times40.render(f"HP: {player.hp}", False, (RED))
 
    
    HJONK_HJONK = pg.sprite.spritecollide(player, enemies, True )
    if HJONK_HJONK:
        print("I am up one, Where did you learn to count we are even")

    screen.blit(bg_img,(0,0))
    all_sprites.draw(screen)
    screen.blit(hp_text,(11,11))

    pg.display.update()

    