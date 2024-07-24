import time,pygame,random
from pygame import display,event,draw,surface

import contoller
import model
import view
pygame.init()

print("кликайте по кирпичам")

while True:
    time.sleep(1/60)
    contoller.controller_start()
    model.model_start()
    view.view_start()




