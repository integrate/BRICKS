import time, pygame
from pygame import display, event, draw,font,rect

import model

pygame.init()


class Circle():
    def __init__(self, x, y,size,speedx,speedy,width,height):
        self.rect_circle=rect.Rect(x - size, y - size, size * 2, size * 2)
        self.speedx=speedx
        self.speedy=speedy
        self.width=width
        self.height=height

    def draw(self, surface):
        draw.circle(surface, [255,37,5], self.rect_circle.center, self.rect_circle.height / 2)
        # draw.rect(surface,[255,255,255],self.rect_circle,3)

    def position_ball(self,ballx,bally):
        self.rect_circle.x=ballx
        self.rect_circle.y=bally

    def move(self,brick_list):
        spisok_rect_brick = [x.rect_brick for x in brick_list]
        self.rect_circle.x+=self.speedx

        if  self.rect_circle.right>= self.width:
            self.rect_circle.right = self.width
            self.speedx = -self.speedx
        if self.rect_circle.left <= 0:
            self.rect_circle.left = 0
            self.speedx = -self.speedx

        touch = self.rect_circle.collidelist(spisok_rect_brick)

        if touch != -1:
            if self.speedx < 0:
                self.rect_circle.left = spisok_rect_brick[touch].right
                self.speedx = -self.speedx
            elif self.speedx > 0:
                self.rect_circle.right = spisok_rect_brick[touch].left
                self.speedx = -self.speedx

            brick_list[touch].reduce_hp_and_remove_brick(brick_list)


        self.rect_circle.y+=self.speedy

        if self.rect_circle.bottom >= self.height:
            self.rect_circle.bottom = self.height
            self.speedy = -self.speedy
        if self.rect_circle.top <= 0:
            self.rect_circle.top = 0
            self.speedy = -self.speedy

        touch = self.rect_circle.collidelist(spisok_rect_brick)

        if touch != -1:
            if self.speedy < 0:
                self.rect_circle.top = spisok_rect_brick[touch].bottom
                self.speedy = -self.speedy
            elif self.speedy > 0:
                self.rect_circle.bottom = spisok_rect_brick[touch].top
                self.speedy = -self.speedy

            brick_list[touch].reduce_hp_and_remove_brick(brick_list)

