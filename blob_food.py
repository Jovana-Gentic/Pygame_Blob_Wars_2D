import pygame, os, random


class Food():
    """
    hi
    """
    def __init__(self, surface_width, surface_height):
        self.surface_width = surface_width
        self.surface_height = surface_height
        
        filepaths = []
        for file in os.listdir('blob_files\\food'):
            filepaths.append(os.path.join('blob_files\\food', file))

        self.food = []
        for snack in filepaths:
            self.food.append(pygame.image.load(snack))
        
        self.food_size = 16,16
        self.position = random.randint(0, self.surface_width-self.food_size[0]), random.randint(0, self.surface_height-self.food_size[1])
        self.idx = random.randint(0,63)
        
    def get_food_pos(self):
        self.position = random.randint(0, self.surface_width-16), random.randint(0, self.surface_height-16)
        self.idx = random.randint(0,63)
    
    def draw(self, surface):
        surface.blit(self.food[self.idx], (self.position[0], self.position[1]))
        return self.position
        
    def get_rectangle(self):
        return pygame.Rect(self.position, self.food_size).center