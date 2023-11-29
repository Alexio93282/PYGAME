import pygame as pg
import random

player_image = pg.image.load("images/VergilDMC5.png")
enemy_image = pg.image.load("images/Dante enemy.jpg")
enemy_image2 = pg.image.load("images/Nero enemy.jpg")
ranged_image = pg.image.load("images/Ebony Ivory.jpg")
bg_img = pg.image.load("images/BG.png")
JCE = pg.image.load("images/Judgement cut.png")

enemy_image = pg.transform.scale(enemy_image,(208,300))
enemy_image2 = pg.transform.scale(enemy_image2,(208,300))
ranged_image = pg.transform.scale(ranged_image,(30,30))
bg_img = pg.transform.scale(bg_img,(2560,1440))
JCE = pg.transform.scale(JCE,(500,500))


STANDING = pg.image.load('images/VergilDMC5.png')
STANDING2 = pg.image.load('images/Idle animation.jpg')
STANDING3 = pg.image.load('images/Idle animation2.jpg')

STANDING2 = pg.transform.scale(STANDING2,(212,460))
STANDING3 = pg.transform.scale(STANDING3,(212,460))

class Player(pg.sprite.Sprite):
    def __init__(self, all_sprites, enemies):
        pg.sprite.Sprite.__init__(self)
        self.current_frame = 0   
        self.last_update = 0 
        self.image = player_image 
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.pos_x = 0
        self.pos_y = 400
        self.speed = 20
        self.hp = 500
        self.all_sprites = all_sprites
        self.enemies = enemies
        self.standing = True 
        self.standing_frames = [STANDING, STANDING2, STANDING3]
        self.attack_cooldown = 0
        self.attack_cooldown2 = 0

        
    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.kill()
        
  
    def animate(self):
        now = pg.time.get_ticks()   # på starten av animate henter vi hvilken "tick" eller frame vi er på 1 tick er 1 FPS
 
        if self.standing:   # vis vi står stille, altså dette er animasjonen vi vil kjøre om vi status for player er "standing"         
            if now - self.last_update > 350:   # her sørger vi for at vi bytte bilde kun hver 350 tick, lavere tall animerer fortere
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()


    def attack(self):
        if self.attack_cooldown == 0:
            self.attack_cooldown = 15
            projectile = ranged_attack(self.pos_x+10, self.pos_y, self.enemies)
            print("Motivation")
            projectile.add(self.all_sprites)

    def cut_end(self):
        if self.attack_cooldown2 == 0:
            self.attack_cooldown2 = 120
            projectile2 = Cut_end(self.pos_x+10, self.pos_y, self.enemies)
            print("Motivation")
            projectile2.add(self.all_sprites)
            
        

    def update(self):
        self.animate()
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.standing= True
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        if self.attack_cooldown2 > 0:
            self.attack_cooldown2 -= 1
        

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
             self.pos_y -= self.speed
        if keys[pg.K_s]:
            self. pos_y += self.speed
        if keys[pg.K_a]:
             self.pos_x -= self.speed
        if keys[pg.K_d]:
             self.pos_x += self.speed
        
        if self.pos_x < 300-self.width:
            self.pos_x = 300-self.width

        if self.pos_x > 2665-self.width:
            self.pos_x = 2665-self.width

        if self.pos_y < 690-self.height:
            self.pos_y = 690-self.height

        if self.pos_y > 1665-self.height:
            self.pos_y = 1665-self.height
       
        if keys[pg.K_SPACE]:
            self.attack()
        
        if keys[pg.K_f]:
            self.cut_end()

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos_x = 1300
        self.pos_y = random.randint(300,1300)
        self.speed = random.randint(1,10)

        self.size_x = 1
        self.size_y = 1
   
        self.max_size_x = 208
        self.max_size_y = 300

        self.moving_in = True


    def update(self):

        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        if not self.moving_in:
            self.pos_x -= self.speed

        else:
         self.size_x   # gjør den større
         self.size_y

         if self.size_x <= self.max_size_x: # if self. size er større eller lik max size
           self.moving_in = False # moving in blir false

        

        if self.pos_x < 0:
            self.kill()       

class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image2
        self.rect = self.image.get_rect()
        self.pos_x = 2600
        self.pos_y = random.randint(300,1300)
        self.speed = random.randint(1,10)
   
    def update(self):
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

        self.pos_x -= self.speed

        if self.pos_x < 0:
            self.kill()

class ranged_attack(pg.sprite.Sprite):
    def __init__(self,x,y, enemies):
        pg.sprite.Sprite.__init__(self)
        self.image = ranged_image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.enemies = enemies

        self.pos_x = x+30
        self.pos_y = y
        self.speed = 10

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
 
        self.pos_x += self.speed

        hits = pg.sprite.spritecollide(self, self.enemies, True)

class Cut_end(pg.sprite.Sprite):
    def __init__(self,x,y, enemies):
        pg.sprite.Sprite.__init__(self)
        self.image = JCE
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255,255,255))
        self.enemies = enemies

        self.pos_x = x+30
        self.pos_y = y
        self.speed = 10

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y 
    
    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
 
        self.pos_x += self.speed

        hits = pg.sprite.spritecollide(self, self.enemies, True)

