import pygame as pg
from Characters import *
 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
 
class Game():
    def __init__(self):
        pg.init()
        
        self.WIDTH = 800
        self.HEIGHT = 600 
        self.FPS = 60
 
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
 
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()
 
        self.new()
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.blocks_grp = pg.sprite.Group()
 
        self.my_player = Player(self, self.all_sprites, self.enemies) 
        self.all_sprites.add(self.my_player)
 
        self.run()
 
        self.new()
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.playing = False
                            
    def update(self):
        self.all_sprites.update()
 
        self.hits = pg.sprite.spritecollide(self.my_player, self.enemies, True)
 
        # spawn enemies max 10
        while len(self.enemies) < 10:
            self.enemy = Enemy()
            self.all_sprites.add(self.enemy)
            self.enemies.add(self.enemy)
 
    def draw(self):
        # tegner ting til skjerm på valgt posisjon, og størrelse
        self.screen.blit(bg_img,(0,0))
        self.all_sprites.draw(self.screen)
 
        # rendrer/generer teksten som vi kan tegne til game screen
        # dette viser ikke teksten enda, men har bare laget den klar
        self.text_player_hp = self.comic_sans30.render(str(self.my_player.hp), False, (RED))
        
        # tegn teksten til skjermen på en satt posisjon
        self.screen.blit(self.text_player_hp, (10, 10))
 
        # oppdaterer alle endringer på spill vinduet
        pg.display.update()
 
        
    def run(self):
        self.playing = True
        while self.playing: # game loop
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()
 
g = Game()