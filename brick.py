import time, pygame
from pygame import display, event, draw, font, rect

pygame.init()


class Brick():
    def __init__(self, x, y, hp, xsize, ysize,reduce_hp_callback):
        self.rect_brick = rect.Rect(x, y, xsize, ysize)
        self.hp = hp
        self.reduce_hp=reduce_hp_callback

    def draw_and_show_hp(self, surface):
        draw.rect(surface, [255, 215, 6], self.rect_brick)
        a = font.Font(None, 20)
        b = a.render(str(self.hp), True, [0, 0, 0])
        surface.blit(b, [self.rect_brick.x + 3, self.rect_brick.y + 3])

    def reduce_hp_and_remove_brick(self, list):
        self.hp -= 1
        if self.hp == 0:
            list.remove(self)
        self.reduce_hp(1)