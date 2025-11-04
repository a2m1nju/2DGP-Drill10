from pico2d import load_image, get_time, load_font

import game_world
import game_framework
from state_machine import StateMachine

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

        self.x = 300
        self.y = 500
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION


    def handle_event(self, event):
        pass

    def draw(self):
        frame_col = int(self.frame) % 5
        frame_row = int(self.frame) // 5
        clip_left = frame_col * 182
        clip_bottom = (2 - frame_row) * 172

        self.image.clip_draw(clip_left, clip_bottom, 180, 150, self.x, self.y, 50, 50)


