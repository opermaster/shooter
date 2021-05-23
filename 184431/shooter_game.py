#Создай собственный Шутер!
import random
from pygame import *
font.init()
mixer.init()


class GameSprite(sprite.Sprite):
    def __init__(self,image,x,y,width,height,name,speed,rect_x,rect_y,enemy_speed):
            sprite.Sprite.__init__(self)
            self.image=image
            self.x=x
            self.y=y
            self.rect_x=rect_x
            self.rect_y=rect_y
            self.width=width
            self.height=height
            self.speed=speed
            self.enemy_speed=enemy_speed
            
    """def print(self):
        self.name=transform.scale(image.load(self.image),(self.width,self.height))
        window.blit(self.name,(self.x,self.y))
    def enemy_print(self):
        self.name=transform.scale(image.load(self.image),(self.width,self.height))
        window.blit(self.name,(self.rect_x,self.rect_y))"""
#ИГРОК
bulets=sprite.Group()
class Player(GameSprite):
    def print(self):
        self.name=transform.scale(image.load(self.image),(self.width,self.height))
        self.rect=self.name.get_rect()
        window.blit(self.name,(self.x,self.y))
    def move(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_a] and self.x>5:
            self.x-=self.speed
        if key_pressed[K_d] and self.x<625:
            self.x+=self.speed
    def fire(self):
        bulet=Bulet("bullet.png",sprit.rect.centerx,sprit.rect.top,5,10,"bullet",10,0,0,0)
        bulets.add(bulet)
        window.blit(bulet)
#ВРАГ
class Enemy(GameSprite):
    def enemy_move(self):
        self.rect_y+=self.enemy_speed
    def enemy_print(self):
        self.name=transform.scale(image.load(self.image),(self.width,self.height))
        self.rect=self.name.get_rect()
        window.blit(self.name,(self.rect_x,self.rect_y))

class Bulet(sprite.Sprite):
    def move(self):
        self.y+=self.speed
        if self.y<0:
            self.kill()

font=font.Font(None,70)
win=font.render("YOU WIN",True,(255,215,0))
lose=font.render("YOU LOSE",True,(255,215,0))



mixer.music.load("space.ogg")
mixer.music.play()

#создай окно игры
window=display.set_mode((700,500))
display.set_caption("Space wars")
#задай фон сцены
bcg=transform.scale(image.load("galaxy.jpg"),(700,500))
#создай 2 спрайта и размести их на сцене
sprit=Player("rocket.png",100,400,60,100,"rocketa",30,0,0,random.randint(1,5))



monsters=sprite.Group()
for i in range(1,6):
    monster=Enemy("ufo.png",random.randint(50,500),0,75,50,"enemy",0,random.randint(1,400),0,random.randint(5,10))
    monsters.add(monster)





game=True
clock=time.Clock()
FPS=60
num_fire=0
#обработай событие «клик по кнопке "Закрыть окно"»
while game:
    key_pressed=key.get_pressed()
    if key_pressed[K_SPACE] and num_fire<5:
        sprit.fire()
    window.blit(bcg,(0,0))
    for m in monsters:
        m.enemy_print()
        m.enemy_move()
    sprit.print()
    sprit.move()
    sprit.fire()
    for e in event.get():
        if e.type==QUIT:
            game=False

        
    clock.tick(FPS)
    display.update()