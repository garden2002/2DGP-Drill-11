import random

from pico2d import *

import game_framework

import game_world
from game_world import collide
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global balls

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    balls = [Ball(random.randint(100, 1500) , 60 ,0) for _ in range(30)]
    game_world.add_objects(balls , 1)

    # 좀비 5마리 추가
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies, 1)

    game_world.add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        game_world.add_collision_pair('boy:ball', None, ball)

    game_world.add_collision_pair('boy:zombie', boy, None)
    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie', None, zombie)


    for zombie in zombies:
        game_world.add_collision_pair('zombie:ball', zombie, None)





def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

    # fill here
    #for ball in balls.copy():
    #   if collide(boy, ball):
    #        print('boy:ball COLLIDE')
    #        #소년 볼 증가
    #        boy.ball_count += 1
    #        game_world.remove_object(ball)
    #        balls.remove(ball)


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

