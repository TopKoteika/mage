from random import choice
from typing import Any
from pygame import *

init()
mixer.init()
font.init
font1 = font.SysFont("impact", 100)
game_over_text  = font1.render("GAME OVER" , True , (255 , 0 , 0))
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(0.0)

MAP_WIDTH, MAP_HEIGHT = 25, 20 # ширина і висота карти
TILESIZE = 40 #розмір квадратика карти
WIDTH, HEIGHT = MAP_WIDTH*TILESIZE, MAP_HEIGHT*TILESIZE

window = display.set_mode((WIDTH,HEIGHT))
FPS = 90
clock = time.Clock()

bg = image.load('background.jpg')
bg = transform.scale(bg,(WIDTH,HEIGHT))

player_img = image.load("hero.png")
wall_img = image.load("wall.png")
gold_img = image.load("treasure.png")
all_sprites = sprite.Group()
cyborg_img = image.load('cyborg.png')

class Sprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = mask.from_surface(self.image)
        all_sprites.add(self)

class Player(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.hp = 100
        self.speed = 4

    def update(self):
        key_pressed = key.get_pressed()
        old_pos = self.rect.x,self.rect.y
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        collide_list = sprite.spritecollide(self , walls , False , sprite.collide_mask)
        if len(collide_list) > 0:
            self.rect.x, self.rect.y = old_pos


        enemys_colide = sprite.spritecollide(self , enemys , False , sprite.collide_mask)
        if len(enemys_colide) >0:
            self.hp -= 100
    

class Ememy(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.damage = 100
        self.speed = 2
        self.dir_list = ['right' , 'left', 'up', 'down']
        self.dir = choice(self.dir_list)


       
    def update(self):
        old_pos = self.rect.x,self.rect.y
        if self.dir =='right':
            self.rect.x += self.speed

        elif self.dir == 'left':
            self.rect.x -= self.speed

        elif self.dir == 'up':
            self.rect.y -= self.speed
        
        elif self.dir == 'down':
            self.rect.y += self.speed


        collide_list = sprite.spritecollide(self , walls , False , sprite.collide_mask)
        if len(collide_list) > 0:
            self.dir = choice(self.dir_list)
            self.rect.x, self.rect.y = old_pos
        





player = Player(player_img, TILESIZE, TILESIZE, 300, 300)
walls = sprite.Group()
enemys = sprite.Group()
with open("map.txt", "r") as f:
    map = f.readlines()
    x = 0
    y = 0
    for line in map:
        for symbol in line:
            if symbol == "w": # стіни
                walls.add(Sprite(wall_img, TILESIZE, TILESIZE, x, y ))
            if symbol == "p": # гравець
                player.rect.x = x
                player.rect.y = y
            if symbol == "g": # стіни
                gold = Sprite(gold_img, 70, 70, x, y )
            if symbol =="e":
                enemys.add(Ememy(cyborg_img, TILESIZE-5, TILESIZE-5, x, y))
                
            x += TILESIZE
        y += TILESIZE
        x = 0
        




run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg,(0,0))

    if player.hp <= 0:
        finish = True

    if sprite.collide_mask(player , gold):
        finish = True
        game_over_text  = font1.render("YOU WIN" , True , (0 , 150 , 0))


    all_sprites.draw(window)
    if not finish:
        all_sprites.update()
    if finish:
        window.blit(game_over_text ,(300,300))
    
    display.update()
    clock.tick(FPS)