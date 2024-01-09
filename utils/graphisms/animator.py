import time

import pygame


class Animator:
    def __init__(self, delay):
        self.n_frames = None
        self.loop = None
        self.animation = None
        self.delay = delay
        self.current_frame = 0
        self.last_update = 0
        self.running = False
        self.flip = 0, 0
        self.rotation = 0

    def update(self):
        if not self.running:
            return None

        if time.time() - self.last_update >= self.delay:
            self.last_update = time.time()
            self.current_frame = (self.current_frame + 1) % self.n_frames

            if not self.loop and self.current_frame == 0:
                self.stop_animation()
                return None

        f_x, f_y = self.flip
        return pygame.transform.rotate(pygame.transform.flip(self.animation.get_frame(self.current_frame), f_x, f_y), self.rotation)

    def start_animation(self, animation, loop=False, at=0):
        self.animation = animation
        self.loop = loop
        self.n_frames = animation.get_frame_num()

        self.running = True
        self.current_frame = at
        self.last_update = time.time()

    def stop_animation(self):
        self.running = False

    def is_animated(self):
        return self.running

    def reset_settings(self):
        self.flip = 0, 0
        self.rotation = 0

    def set_settings(self, flip=(0, 0), rotation=0):
        self.flip = flip
        self.rotation = rotation
