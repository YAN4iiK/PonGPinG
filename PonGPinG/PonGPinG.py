
from pygame import *
from random import randint
from time import time as timer

#Класс спрайта
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, w, h, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Класс игрока
class Player(GameSprite):
    def update(self):
        global frame
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= 5
        if keys_pressed[K_d] and self.rect.x < 750:
            self.rect.x += 5

#Окно игры
window = display.set_mode((800,600))
display.set_caption('PonGPinG')
#Фон сцены
bg = transform.scale(image.load('bg.jpg'), (800,600))

#Переменные
clock = time.Clock()
FPS = 74

font.init()

lose = font.SysFont('Areal', 76).render('Поражение', True, (255, 255, 255))
win =  font.SysFont('Areal', 76).render('Победа', True, (255, 255, 255))


'''#Музыка
mixer.init()
#mixer.music.load('doom.ogg')
#mixer.music.play()
fire = mixer.Sound('fire.ogg')'''



run = True
finish = False

while run:
#Завершение игры
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not(finish):
        window.blit(bg, (0,0))


    display.update()
    clock.tick(FPS)
    new_time = timer()


