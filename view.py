import time,pygame,random
from pygame import display,event,draw,surface,font,rect

import model
import settings,brick,circle
pygame.init()

window=display.set_mode([settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT])
window_name=display.set_caption("Bricks")

picture=surface.Surface([settings.WINDOW_WIDTH,settings.WINDOW_HEIGHT])
picture.fill([139,253,255])

a = font.Font(None, 40)
pr = font.Font(None, 40)
q = font.Font(None, 38)
w = q.render("ball", True, [81, 255, 16])

def view_start():

    window.blit(picture,[0,0])
    b = a.render(str(int(model.coin)), True, [0, 0, 0])
    window.blit(b, [settings.WINDOW_WIDTH-50,10])

    ize = pr.render(str(int(model.prize)), True, [255, 104, 0])
    window.blit(ize, [settings.WINDOW_WIDTH-50,73])

    draw.rect(window,[251,0,255],model.button)
    window.blit(w, [settings.WINDOW_WIDTH - 58, 43])

    for cube in model.spisok_cube:
        cube.draw_and_show_hp(window)

    for ball in model.spisok_ball:
        ball.draw(window)

    display.flip()
