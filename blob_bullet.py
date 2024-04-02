import pygame, math

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, start_x, start_y, target_x, target_y, bullet_image):
        super().__init__()
        self.image = bullet_image
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.target_x = target_x
        self.target_y = target_y
        self.velocity = self.calculate_velocity()
        self.speed = 5
    
    # Calculate bullet's coordinate changes based on target's position using The Euclidean distance
    def calculate_velocity(self):
        dx = self.target_x - self.rect.centerx
        dy = self.target_y - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance == 0:
            return 0, 0  
        self.speed = 5
        return round(dx / distance * self.speed), round(dy / distance * self.speed)

    def update(self):
        self.rect.move_ip(self.velocity)
