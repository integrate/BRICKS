import time,pygame,random
from pygame import display,event,draw,surface

import model
pygame.init()

def controller_start():
    events = event.get()
    for x in events:
        if x.type==pygame.MOUSEBUTTONDOWN and x.button==pygame.BUTTON_LEFT:
            model.hp_reduce_click(x.pos)
            model.press_button(x.pos)

    for x in events:
        if x.type == pygame.QUIT:
            exit()