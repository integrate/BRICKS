import time, pygame, random,math
from pygame import display, event, draw, surface, rect
from random import choice

import settings, brick, circle


def model_start():
    if spisok_cube==[]:
        create_new_level()
        for ball in spisok_ball:
            ball.position_ball(ballx,bally)

    for ball in spisok_ball:
        ball.move(spisok_cube)


def hp_reduce_click(xy_pos):
    for cube in spisok_cube:
        if cube.rect_brick.collidepoint(xy_pos):
            cube.reduce_hp_and_remove_brick(spisok_cube)



def press_button(xy_pos):
    if button.collidepoint(xy_pos):
        create_ball()


def create_ball():
    global prize
    if coin<prize:
        return
    minus_coin()
    prize=round((prize/100)*110,0)
    a1 = random.randint(1, 3)
    b1=math.sqrt(16-(a1*a1))
    a=random.choice([a1,-a1])
    b=random.choice([b1,-b1])
    ball = circle.Circle(ballx, bally, 15, a, b, settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
    spisok_ball.append(ball)


def plus_coin(money):
    global coin
    coin += money


def minus_coin():
    global coin
    coin -= prize


pygame.init()

spisok_cube = []
spisok_ball = []
number_cube_in_row = 0
coin = 0
prize=10
hp=0
level=0
ballx=30
bally=30

x_start_in_def=0
y_start_in_def=0
y_size_cube_in_def=0
number_cube_for_break=0
number_range_for_column=0


x_start = (settings.WINDOW_WIDTH - ((settings.width_cube * 5) + (settings.range_column * 4))) // 2
y_size_cube = ((settings.WINDOW_HEIGHT - 20) - 14 * settings.range_row) // 15
y_start = (((settings.WINDOW_HEIGHT - 20) - ((y_size_cube * 15) + (settings.range_row * 14))) // 2)+10

x_start2 = (settings.WINDOW_WIDTH - ((settings.width_cube * 9) + (settings.range_column * 8))) // 2
y_size_cube2 = ((settings.WINDOW_HEIGHT - 20) - 7 * settings.range_row) // 8
y_start2 = (((settings.WINDOW_HEIGHT - 20) - ((y_size_cube2 * 8) + (settings.range_row * 7))) // 2)+10


x_start3 = (settings.WINDOW_WIDTH - ((settings.width_cube * 12) + (settings.range_column *11))) // 2
y_size_cube3 = (((settings.WINDOW_HEIGHT//2)-20) - 5 * settings.range_row) // 6
y_start3 = (settings.WINDOW_HEIGHT//2)+10


x_start4 = (settings.WINDOW_WIDTH//2)+(((settings.WINDOW_WIDTH//2) - ((settings.width_cube * 7) +\
                                                                      (settings.range_column *6)))//2)
y_size_cube4 = (((settings.WINDOW_HEIGHT//2)-20) - 9* settings.range_row) // 10
y_start4 = (settings.WINDOW_HEIGHT//2)+10


x_start5 = ((settings.WINDOW_WIDTH//2) - ((settings.width_cube * 7) +(settings.range_column *6)))//2
y_size_cube5 = (((settings.WINDOW_HEIGHT//2)-20) - 9* settings.range_row) // 10
y_start5 = (settings.WINDOW_HEIGHT//2)+10


x_start6 = ((settings.WINDOW_WIDTH//2) - ((settings.width_cube * 7) +(settings.range_column *6)))//2
y_size_cube6 = (((settings.WINDOW_HEIGHT//2)-20) - 9* settings.range_row) // 10
y_start6 = 10


def create_new_level():
    global hp,level,number_cube_in_row,ballx,bally,x_start_in_def,y_start_in_def,y_size_cube_in_def,\
        number_cube_for_break,number_range_for_column

    hp+=1
    level += 1

    if level==1:
        ballx=30
        bally=30
        x_start_in_def=x_start
        y_start_in_def=y_start
        y_size_cube_in_def=y_size_cube
        number_cube_for_break=15
        number_range_for_column=6

    if level == 2:
        x_start_in_def = x_start2
        y_start_in_def = y_start2
        y_size_cube_in_def = y_size_cube2
        number_cube_for_break=8
        number_range_for_column=10


    if level == 3:
        x_start_in_def = x_start3
        y_start_in_def = y_start3
        y_size_cube_in_def = y_size_cube3
        number_cube_for_break=6
        number_range_for_column=13


    if level == 4:
        x_start_in_def = x_start4
        y_start_in_def = y_start4
        y_size_cube_in_def = y_size_cube4
        number_cube_for_break=10
        number_range_for_column=8


    if level == 5:
        x_start_in_def = x_start5
        y_start_in_def = y_start5
        y_size_cube_in_def = y_size_cube5


    if level == 6:
        level=0
        ballx=500
        bally=500
        x_start_in_def = x_start6
        y_start_in_def = y_start6
        y_size_cube_in_def = y_size_cube6


    for column_bricks in range(1, number_range_for_column):
        for row_bricks in range(y_start_in_def, settings.WINDOW_HEIGHT, y_size_cube_in_def + settings.range_row):
            number_cube_in_row += 1
            q = brick.Brick(x_start_in_def, row_bricks, hp, settings.width_cube, y_size_cube_in_def, plus_coin)
            spisok_cube.append(q)

            if number_cube_in_row == number_cube_for_break:
                number_cube_in_row = 0
                x_start_in_def += settings.width_cube + settings.range_column
                break



button = rect.Rect(settings.WINDOW_WIDTH - 60, 40, 50, 30)

