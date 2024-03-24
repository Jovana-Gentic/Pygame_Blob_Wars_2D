import pygame
import random

food_sounds = ['blob_files\music\\apple-munch.mp3',
               'blob_files\music\carrotnom.mp3',
               'blob_files\music\crunchy.mp3',
               'blob_files\music\\nibbling.mp3']


    

class Sounds():
    def __init__(self):
        pygame.mixer.init()
        self.background_music = pygame.mixer.Sound('blob_files\music\music.mp3')
        self.ch1 = pygame.mixer.Channel(1)
        self.ch1.set_volume(0.1)
        self.ch1.play(self.background_music, loops=-1)
        self.ch2 = pygame.mixer.Channel(2)
        self.sounds = []
        for sound in food_sounds:
            self.sounds.append(pygame.mixer.Sound(sound))
            
            
    def eating_sounds(self):
        self.ch2.play(self.sounds[random.randint(0,3)])
        