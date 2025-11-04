from pico2d import load_image, get_time, load_font

import game_world
import game_framework
import random
from state_machine import StateMachine

PIXELS_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 35
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXELS_PER_METER)

TIME_PER_ACTION = 1.0 / 13.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

        self.x = random.randint(50, 750)
        self.y = 500
        self.dir = 1
        self.speed = RUN_SPEED_PPS
        self.frame = random.randint(0, 13)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.dir * self.speed * game_framework.frame_time

        if self.x < 25:
            self.x = 25
            self.dir = 1
        elif self.x > 1570:
            self.x = 1570
            self.dir = -1

    def handle_event(self, event):
        pass

    def draw(self):
        frame_col = int(self.frame) % 5
        frame_row = int(self.frame) // 5
        clip_left = frame_col * 182
        clip_bottom = (2 - frame_row) * 172

        if self.dir == 1:
            self.image.clip_draw(clip_left, clip_bottom, 180, 150, self.x, self.y, 30, 30)
        else:
            self.image.clip_composite_draw(clip_left, clip_bottom, 180, 150, 0, 'h', self.x, self.y, 30, 30)


