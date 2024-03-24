import pygame, random
from blob import *
from blob_utils import *
from blob_food import *
from blob_menu import *
import os

pygame.init()

pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.display.set_caption('Blob Wars')

# SCREEN
screen_width = 600
screen_height = 700
screen_color = 139, 163, 147
screen = pygame.display.set_mode((screen_width,screen_height))

#SURFACE
surface_width = 550
surface_height = 550
surface_color = 255, 221, 163
surface = pygame.Surface((surface_width, surface_height))
bound = surface.get_rect()
surface_background = pygame.image.load('blob_files\grass.PNG').convert()
screen_background = pygame.image.load('blob_files\stone.png').convert()
outline_color = 32, 38, 34

#CREATE BLOB
blob = Blob(f'blob_files\\blobs\\blob{random.randint(1,12)}.png', surface, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, size = (75,65))
blob2 = Blob(f'blob_files\\blobs\\blob{random.randint(1,12)}.png', surface, pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l, size = (75,65))

#SET SOUNDS
sound = Sounds()

#FOOD
food = Food(surface_width, surface_height)

#MENU
menu = Menu(screen)

FPS = 100
clock = pygame.time.Clock()

running = True
menu_open = False
esc_pressed = False
while running:
    clock.tick(FPS)
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
        menu.stop = True
       
    if menu.stop:
        menu.call(screen, screen_background, sound.ch1)
        
    else:        
        screen.blit(screen_background,(0,0))
        pygame.draw.rect(screen, outline_color, (20,20,560,560), 5)
        surface.blit(surface_background,(0,0))
        
        fx, fy = food.draw(surface)
        
        blob.x, blob.y = blob.move()
        blob2.x, blob2.y = blob2.move()
        
        if blob.eats_food(food.get_rectangle()):
            blob.update_score()
            sound.eating_sounds()
            food.get_food_pos()
            
        if blob2.eats_food(food.get_rectangle()):
            blob2.update_score()
            sound.eating_sounds()
            food.get_food_pos()
        
        
        blob.draw(surface, (blob.x, blob.y))
        blob2.draw(surface, (blob2.x, blob2.y))
        screen.blits([(surface,(25,25))])
        pygame.display.update()

