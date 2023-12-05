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

attack = pg.sprite.Group()

player = Player(all_sprites, enemies, attack)

enemy = Enemy()
enemy2 = Enemy2()

rangedAttack = ranged_attack(1, 1, enemies, attack)

all_sprites.add(player)
all_sprites.add(enemy)

all_sprites.add(rangedAttack)

enemies.add(enemy2)

enemies.add(enemy)

attack.add(rangedAttack)

spawning_enemy = pg.sprite.Group()
all_sprites.add(spawning_enemy)
#spawning_enemy.add(enemy)



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
        

    for obj in enemies:
        if obj.moving_in == False:
            enemies.add(obj)

    all_sprites.update()

    hp_text = font_times40.render(f"HP: {player.hp}", False, (RED))
    hits = pg.sprite.spritecollide(player, enemies, False)

    if hits:
        for key in hits:
            if not key.moving_in:
                player.hp -= 10
                player.take_dmg(10)

                key.kill()
                print("I am up one, Where did you learn to count we are even")
                print("HP:",player.hp)
            else:
                print("enemy currently spawning, no damage taken :)")
        


    screen.blit(bg_img,(0,0))
    all_sprites.draw(screen)
    screen.blit(hp_text,(11,11))

    pg.display.update()

