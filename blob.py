import pygame

class Blob(pygame.sprite.Sprite):
    def __init__(self, filepath, surface, up, down, left, right, size=None):
        super().__init__()
        
        self.up, self.down, self.left, self.right = up, down, left, right
        
        self.image = pygame.image.load(filepath).convert_alpha()
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.image_left = self.image.copy()
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.w, self.h = self.image.get_size() 
        self.x = surface.get_width()//2
        self.y = surface.get_height()//2
        self.size = size
        self.bound = surface.get_rect()
        self.speed = 1
        self.score = 0
        
    def draw(self, surface, pos):
        surface.blit(self.image, (self.x, self.y))
        
    def move(self):
        #value = self.bound.contains(pygame.Rect(self.x, self.y, self.w, self.h))
        # pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s
        if pygame.key.get_pressed()[self.right] and self.x<(self.bound[2]-self.size[0]):
            self.x += self.speed
            self.image = self.image_right
        if pygame.key.get_pressed()[self.left] and self.x>self.bound[1]:
            self.x -= self.speed
            self.image = self.image_left
        if pygame.key.get_pressed()[self.up] and self.y>self.bound[0]:
            self.y -= self.speed
        if pygame.key.get_pressed()[self.down] and self.y<(self.bound[3]-self.size[1]):
            self.y += self.speed

        return self.x, self.y
    
    def get_rectangle(self):
        return pygame.Rect(self.x, self.y, *self.size)
        
    def eats_food(self, food):
        rect = self.get_rectangle()
        return rect.collidepoint(food)
        
    def update_score(self):
        self.score += 1
            
