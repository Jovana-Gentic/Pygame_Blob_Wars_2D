import pygame, random
from params import *

class Sounds:
    def __init__(self):
        pygame.mixer.init()
        
        self.background_music = pygame.mixer.Sound(background_music)
        self.ch1 = pygame.mixer.Channel(1)
        self.ch1.set_volume(0.1)
        self.ch1.play(self.background_music, loops=-1)
        
        self.ch2 = pygame.mixer.Channel(2)
        self.sounds = [pygame.mixer.Sound(sound) for sound in food_sounds]
        self.ch2.set_volume(0.4)       
       
        self.menu_click = pygame.mixer.Sound(menu_click)
        self.speed_sound = pygame.mixer.Sound(speed_sound)
        self.ch3 = pygame.mixer.Channel(3) 
        self.ch3.set_volume(0.2)
        
        self.shoot_sound = pygame.mixer.Sound(shoot_sound)
        self.shieldpop_sound = pygame.mixer.Sound(shieldpop_sound)
        self.magnet_sound = pygame.mixer.Sound(magnet_sound)
        self.ouch_sound = pygame.mixer.Sound(ouch_sound)
        self.ough_sound = pygame.mixer.Sound(ough_sound)
        
        self.ch4 = pygame.mixer.Channel(4) 
        self.ch4.set_volume(0.5)

        self.ch0 = pygame.mixer.Channel(0) 
        self.ch0.set_volume(0.05)
        
    def play_eating_sound(self):
        self.ch2.play(random.choice(self.sounds))
        
    def play_menu_sound(self):
        self.ch3.play(self.menu_click, loops=0)
        
    def play_shoot_sound(self):
        self.ch4.play(self.shoot_sound, loops=0)

    def play_shieldpop_sound(self):
        self.ch4.play(self.shieldpop_sound, loops=0)
        
    def play_magnet_sound(self):
        self.ch4.play(self.magnet_sound, loops=0)
        
    def play_ouch_sound(self):
        self.ch4.play(self.ouch_sound, loops=0)
        
    def play_hit_sound(self):
        self.ch0.play(self.ough_sound, loops=0)
        
    def play_speed_sound(self):
        self.ch3.play(self.speed_sound, loops=0)