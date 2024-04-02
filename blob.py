import pygame
from params import *
from blob_sounds import Sounds
from blob_bullet import Bullet

class Blob():
    
    def __init__(self, character_filepath, bullet_filepath, shield_filepath, dizzy_filepath, surface,x, y, up, down, left, right,
                 shield_key, speed_boost_key,shoot_key, magnet_key, player_name, is_blob2):
        self.player_name = player_name
        self.up, self.down, self.left, self.right = up, down, left, right 
        self.speed_boost_key, self.shield_key, self.shoot, self.magnet_key =   shield_key, shoot_key, magnet_key, speed_boost_key
        self.x = x
        self.y = y
        self.size = (70, 60)
        self.rect = self.update_rectangle()
        self.load_images(character_filepath, shield_filepath, speed_image, magnet_filepath, bullet_filepath, dizzy_filepath)
        
        self.surface = surface
        self.bound = surface.get_rect()
        
        self.has_shield = 0
        self.shield_active = False
        self.shield_timer = 0

        self.has_speed_boost = 0
        self.speed_boost_active = False
        self.speed_boost_timer = 0
        self.speed = 1
        
        self.score = 0
        self.bullets = pygame.sprite.Group()
        self.shooting_active = False
        self.shooting_timer = 0
        self.is_blob2 = is_blob2
        
        self.has_magnet = 0
        self.magnet_active = False
        self.magnet_timer = 0
           
        self.trapped = False
        self.trap_start_timer = 0
        self.trap_duration = 200
        
        self.sound = Sounds()

    def load_images(self, character_filepath, shield_filepath, speed_image, magnet_filepath, bullet_filepath, dizzy_filepath):
        self.image = pygame.image.load(character_filepath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.image_left = self.image.copy()
        self.image_right = pygame.transform.flip(self.image, True, False)
        self.shield_image = pygame.image.load(shield_filepath).convert_alpha()
        self.speed_boost_image = pygame.image.load(speed_image).convert_alpha()
        self.magnet_image = pygame.image.load(magnet_filepath).convert_alpha()     
        self.bullet_image = pygame.image.load(bullet_filepath).convert_alpha()
        self.dizzy_image = pygame.image.load(dizzy_filepath).convert_alpha()
        
    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        if self.trapped:
            self.surface.blit(self.dizzy_image, (self.x-15, self.y-15))
    
    def move(self):
        if self.trapped == False:
            self.rect = self.update_rectangle()

            if pygame.key.get_pressed()[self.right] and self.x < self.bound[2] - self.size[0]:
                self.image = self.image_right
                self.x += self.speed
                    
            if pygame.key.get_pressed()[self.left] and self.x > self.bound[1]:
                self.image = self.image_left
                self.x -= self.speed
                    
            if pygame.key.get_pressed()[self.up] and self.y > self.bound[0]:
                self.y -= self.speed
                
            if pygame.key.get_pressed()[self.down] and self.y < self.bound[3] - self.size[1]:
                self.y += self.speed

        return self.x, self.y
    
    def update_rectangle(self):
        return pygame.Rect(self.x, self.y, *self.size)
        
    def eats_food(self, food):
        return self.rect.collidepoint(food)
        
    def update_score(self):
        self.score += 1
        
    def apply_trap(self, frame_counter):
        self.score -= 1
        self.trap_start_timer = frame_counter
        self.sound.play_ouch_sound()    

    def remove_trap(self, frame_counter):
        if frame_counter == (self.trap_start_timer +  self.trap_duration) and self.trapped == True:
            self.trapped = False
   
    def use_magnet(self, frame_counter):
        if self.magnet_active==False and self.has_magnet > 0 and pygame.key.get_pressed()[self.magnet_key] and self.trapped == False:
            self.has_magnet -= 1
            self.magnet_active = True
            self.magnet_timer = frame_counter
            
    # Apply magnet for 200 frames           
    def apply_magnet(self, frame_counter):
        if self.magnet_active == True and frame_counter <= self.magnet_timer + 100:       
            magnet_xy = self.magnet_image.get_rect(bottomright=self.rect.bottomright)
            self.surface.blit(self.magnet_image, magnet_xy)
            if frame_counter == self.magnet_timer:
                self.sound.play_magnet_sound() 
        else:
            self.magnet_active = False

               
    def use_shield(self, frame_counter):
        if self.shield_active==False and self.has_shield > 0 and pygame.key.get_pressed()[self.shield_key] and self.trapped == False:
            self.has_shield -= 1
            self.shield_active = True
            self.shield_timer = frame_counter
            
    # Apply shield for 200 frames          
    def apply_shield(self, frame_counter):
        if self.shield_active == True and frame_counter <= self.shield_timer + 200:       
            shield_image_xy = self.shield_image.get_rect(center=self.rect.center)
            self.surface.blit(self.shield_image, shield_image_xy)
            if frame_counter == self.shield_timer +200:
                self.sound.play_shieldpop_sound()
        else:
            self.shield_active = False

    def use_speed_boost(self, frame_counter):
        if not self.speed_boost_active and self.has_speed_boost > 0 and pygame.key.get_pressed()[self.speed_boost_key] and self.trapped == False:
            self.has_speed_boost -= 1
            self.speed_boost_active = True
            self.speed_boost_timer = frame_counter
            self.sound.play_speed_sound()
    
    # Apply speed boost for 200 frames        
    def apply_speed_boost(self, frame_counter):
        if self.speed_boost_active and frame_counter <= self.speed_boost_timer + 200:       
            self.speed = 1.5
            speed_boost_xy = self.speed_boost_image.get_rect(center=self.rect.center)
            self.surface.blit(self.speed_boost_image, speed_boost_xy)
        else:
            self.speed_boost_active = False
            self.speed = 1
            
    def shoot_bullet(self, start_x, start_y, target_x, target_y, frame_counter, target_hp_width, target_hp_x,
                     shield_rect, shield_active):
        if pygame.key.get_pressed()[self.shoot] and self.shooting_active == False and self.score>0 and self.trapped == False:  # Shoot bullets if avaliable
            self.shooting_active = True
            self.shooting_timer = frame_counter
            bullet = Bullet(start_x, start_y, target_x, target_y, self.bullet_image)
            self.bullets.add(bullet)
            self.sound.play_shoot_sound()
        if self.shooting_active == True and frame_counter == self.shooting_timer + 100:  # Add 100 frames delay between shots
            self.shooting_active = False 
            
        target_hp_width, target_hp_x, shield_active = self.update_bullets(target_x, target_y, target_hp_width,
                                                                          target_hp_x, shield_rect, shield_active)
        self.draw_bullets()
        return target_hp_width, target_hp_x, shield_active
    
    def update_bullets(self, target_x,target_y,target_hp_width, target_hp_x, shield_rect, shield_active):
        for bullet in self.bullets:
            if bullet.rect.colliderect(shield_rect) and shield_active == True:  # Removes target's shield and bullet if bullet collides with it
                self.score -= 1
                self.bullets.remove(bullet)
                shield_active = False
                self.sound.play_shieldpop_sound()
            elif bullet.rect.colliderect(target_x-70//2, target_y-60//2, 70, 60):  # Removes target's health and bullet if bullet collides with target
                self.score -= 1
                self.bullets.remove(bullet)
                target_hp_width -=10
                if self.is_blob2 == True:
                    target_hp_x += 10
                self.sound.play_hit_sound()
            else:
                shield_active = shield_active
            if bullet.rect.colliderect(self.surface.get_rect()):  # Check if bullet is still on the screen
                bullet.update()
            else:
                self.bullets.remove(bullet)  # Remove bullet if it leaves the screen
        return target_hp_width, target_hp_x, shield_active
    
    def draw_bullets(self):
        self.bullets.draw(self.surface)  # Draw all bullets on the screen