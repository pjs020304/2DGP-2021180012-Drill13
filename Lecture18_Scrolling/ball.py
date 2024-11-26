from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            self.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

        # self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)

    def update(self):



        if clamp(get_canvas_width()/2, server.boy.x, server.background.w - get_canvas_width()/2) == server.boy.x:
            self.x -= math.cos(server.boy.dir) * server.boy.speed * game_framework.frame_time
        if clamp(get_canvas_height()/2, server.boy.y, server.background.h - get_canvas_height()/2) == server.boy.y:
            self.y -= math.sin(server.boy.dir) * server.boy.speed * game_framework.frame_time
        pass


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)

