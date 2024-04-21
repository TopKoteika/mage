from typing import Any
from pygame import *

init()
mixer.init()
mixer.music.load('qwe.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
WIDTH , HEIGHT = 900 , 700
window = display.set_mode((WIDTH,HEIGHT))
FPS = 90
clock = time.Clock()

bg = image.load('background.jpg')
bg = transform.scale(bg,(1100,750))
hero_img = image.load('hero.png')
cyborg_img = image.load('cyborg.png')
treasure_img = image.load('treasure.png')
wall_img = image.load('wall.png')


all_sprites = sprite.Group()
class Sprite(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__()
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        all_sprites.add(self)

class Player(Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        super().__init__(sprite_img, width, height, x, y)
        self.hp = 100
        self.speed = 4


    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >0:
            self.rect.y -= self.speed
        if key_pressed[K_a]and self.rect.x >0:
            self.rect.x -= self.speed
        if key_pressed[K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if key_pressed[K_d] and self.rect.right <WIDTH:
            self.rect.x += self.speed
        
        


    



Player = Player(hero_img, 70 , 70 , 300 , 300)


run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg,(0,0))
    all_sprites.draw(window)
    all_sprites.update()
   
    
    display.update()
    clock.tick(FPS)


