import pygame as pg
import random

player_image = pg.image.load("images/VergilDMC5.png")
enemy_image = pg.image.load("images/Dante enemy.jpg")
ranged_image = pg.image.load("images/Ebony Ivory.jpg")

enemy_image = pg.transform.scale(enemy_image,(208,300))
ranged_image = pg.transform.scale(ranged_image,(30,30))

class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image 
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = 400
        self.speed = random.randint(15,15)
        self.all_sprites = all_sprites

    def attack(self):
        projectile = ranged_attack(self.pos_x, self.pos_y)
        print("Motivation")
        projectile.add(self.all_sprites)


    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
             self.pos_y -= self.speed
        if keys[pg.K_s]:
            self. pos_y += self.speed
        if keys[pg.K_a]:
             self.pos_x -= self.speed
        if keys[pg.K_d]:
             self.pos_x += self.speed
       
        if keys[pg.K_SPACE]:
            self.attack()
        

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 900
        self.pos_y = random.randint(0,600)
        self.speed = random.randint(1,10)
   
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        self.pos_x -= self.speed

        if self.pos_x > 1205:
            self.kill()

class ranged_attack(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))

        self.pos_x = x
        self.pos_y = y
        self
        self.speed = 10

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
 
        self.pos_x += self.speed