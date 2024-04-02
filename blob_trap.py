import pygame, random
from params import *

class Trap():
    def __init__(self, surface_width, surface_height):
        self.surface_width = surface_width
        self.surface_height = surface_height
        self.trap_image = pygame.image.load(trap_path).convert_alpha()
        self.trap_size = 32, 32
        self.generate_position(frame_counter = 0)
        self.trap_active = True
    
    def generate_position(self, frame_counter):
        self.trap_x = random.randint(0, self.surface_width - self.trap_size[0]) 
        self.trap_y = random.randint(0, self.surface_height - self.trap_size[1])
        self.rect = pygame.Rect(self.trap_x, self.trap_y, *self.trap_size)
        self.start_timer = frame_counter + random.randint(100, 200)
        self.end_timer = self.start_timer + random.randint(100, 400)

    def draw(self, surface, frame_counter):
        if frame_counter == self.end_timer:
            self.generate_position(frame_counter) 
            self.trap_active = False
        if frame_counter >= self.start_timer:
            surface.blit(self.trap_image, (self.trap_x, self.trap_y))
            self.trap_active = True
