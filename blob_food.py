import pygame, os, random, math
from params import *

class Food:
    def __init__(self, surface_width, surface_height):
        self.surface_width = surface_width
        self.surface_height = surface_height
        
        self.food = self.load_food_images()
        
        self.food_size = (16, 16)
        self.food_x, self.food_y = self.generate_position()
        
        self.probabilities = [0.5/64] * 64 + [0.1, 0.3, 0.1] # Probabilities from which we sample food/abilities
        self.indices = list(range(len(self.probabilities)))
        self.idx = int(random.choices(self.indices, self.probabilities, k=1)[0])
        
        self.magnet = 64
        self.shield = 65
        self.speed_boost = 66
        
    def load_food_images(self):
        food = []
        filepaths = [os.path.join(food_files, file) for file in os.listdir(food_files)]
        for snack in filepaths:
            food.append(pygame.image.load(snack).convert_alpha())
        return food
    
    def generate_position(self):
        return random.randint(0, self.surface_width - self.food_size[0]), random.randint(0, self.surface_height - self.food_size[1])
    
    def get_food_pos(self):
        self.idx = int(random.choices(self.indices, self.probabilities, k=1)[0])
        if self.idx == self.speed_boost or self.idx == self.shield or self.idx == self.magnet:
            self.food_size = 32, 32
        else: 
            self.food_size = 16, 16
        self.food_x, self.food_y = self.generate_position()
       
    
    def draw(self, surface, blob_x, blob_y, blob2_x, blob2_y, blob_magnet_active, blob2_magnet_active):
        
        if blob_magnet_active:    
            dx, dy= calculate_food_velocity(blob_x+35, blob_y+30, self.food_x, self.food_y)
            self.food_x, self.food_y = self.food_x+dx, self.food_y+dy
        if blob2_magnet_active:
            dx, dy= calculate_food_velocity(blob2_x+35, blob2_y+30, self.food_x, self.food_y)
            self.food_x, self.food_y = self.food_x+dx, self.food_y+dy
        
        surface.blit(self.food[self.idx], (self.food_x, self.food_y))
        return self.idx
    
    def get_coordinates(self):   
        return pygame.Rect(self.food_x, self.food_y, *self.food_size).center

def calculate_food_velocity(blob_x, blob_y, food_x, food_y):
    dx = blob_x - food_x
    dy = blob_y - food_y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    if distance == 0:
        return 0, 0  
    speed = 2
    return dx / distance * speed, dy / distance * speed