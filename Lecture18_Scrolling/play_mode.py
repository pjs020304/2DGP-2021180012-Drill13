import random
import json
import os

from pico2d import *
import game_framework
import game_world

import server
from boy import Boy
from ball import Ball

# fill here
from background import NewFixedBackground as Background



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)



def init():
    server.background = Background()
    game_world.add_object(server.background, 0)
    server.boy = Boy()
    game_world.add_object(server.boy, 1)
    game_world.add_collision_pair('boy:ball', server.boy, None)


    balls = [Ball() for i in range(100)]
    for o in balls:
        game_world.add_object(o, 1)
        game_world.add_collision_pair('boy:ball', None, o)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass



