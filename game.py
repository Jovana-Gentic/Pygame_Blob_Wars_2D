import pygame
from blob import Blob
from blob_sounds import Sounds
from blob_food import Food
from blob_menu import Menu
from blob_hp_bar import HPBar
from blob_ability_bar import AbilityBar
from blob_trap import Trap
from params import *

pygame.init()

pygame.mouse.set_cursor(*pygame.cursors.diamond)
pygame.display.set_caption('Blob Wars')
pygame.display.set_icon(pygame.image.load(logo))

# SCREEN
screen_width = 600
screen_height = 700
screen_color = 139, 163, 147
screen = pygame.display.set_mode((screen_width,screen_height))

# SURFACE
surface_width = 550
surface_height = 550
surface_color = 255, 221, 163
surface = pygame.Surface((surface_width, surface_height))
bound = surface.get_rect()
surface_background = pygame.image.load(surface_image_path).convert()
screen_background = pygame.image.load(screen_image_path).convert()
screen_background2 = pygame.image.load(screen_image_path2).convert()
outline_color = 33, 41, 33

# INITIALIZE BLOBS
blob_height, blob_width = 60,70
blob = Blob(red_blob_image, 
            red_bullet_path,
            red_shield_path,
            red_dizzy_filepath,
            surface, 
            bound.centerx-blob_height//2, 
            0, 
            up = pygame.K_w, 
            down = pygame.K_s, 
            left = pygame.K_a, 
            right = pygame.K_d,
            shield_key = pygame.K_q, 
            speed_boost_key = pygame.K_e,
            shoot_key= pygame.K_r, 
            magnet_key=pygame.K_f,
            player_name = 'Blobby',
            is_blob2 = True)
blob2 = Blob(blue_blob_image,
             blue_bullet_path,
             blue_shield_path,
             blue_dizzy_filepath,
             surface,
             bound.centerx-blob_height//2,
             surface_height-blob_width,  
             up =pygame.K_i,
             down =pygame.K_k,
             left =pygame.K_j, 
             right =pygame.K_l,
             shield_key = pygame.K_u, 
             speed_boost_key =pygame.K_o, 
             shoot_key= pygame.K_p,
             magnet_key=pygame.K_SEMICOLON,
             player_name = 'Blobster',
             is_blob2 = False)

# INITIALIZE SOUNDS
sound = Sounds()

# INITIALIZE FOOD
food = Food(surface_width, surface_height)

# INITIALIZE MENU
menu = Menu(screen, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d,  pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l, )

# INITIALIZE SCORE
ability_bar = AbilityBar(blob.player_name, blob2.player_name, 
              blob.shield_key, blob2.shield_key, 
              blob.speed_boost_key, blob2.speed_boost_key, 
              blob.shoot, blob2.shoot, 
              blob.magnet_key, blob2.magnet_key)

# INITIALIZE HP BAR
hp_bar = HPBar(screen, 25, 585, 
               blob.player_name, blob2.player_name)

# INITIALIZE TRAPS
trap = Trap(surface_height, surface_width)

FPS = 100
clock = pygame.time.Clock()

running = True
frame_counter = 0

while running:
    clock.tick(FPS)
    frame_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
        menu.paused = True    

    if menu.paused:
        running, menu.restart,blob.up,  blob.down, blob.left,blob.right, blob2.up,  blob2.down, blob2.left, blob2.right = menu.call(screen, screen_background2, sound.ch1)

        if menu.restart == True:
            blob = Blob(red_blob_image, 
                        red_bullet_path,
                        red_shield_path,
                        red_dizzy_filepath,
                        surface, 
                        bound.centerx-blob_height//2, 
                        0, 
                        up = pygame.K_w, 
                        down = pygame.K_s, 
                        left = pygame.K_a, 
                        right = pygame.K_d,
                        shield_key = pygame.K_q, 
                        speed_boost_key = pygame.K_e,
                        shoot_key= pygame.K_r, 
                        magnet_key=pygame.K_f,
                        player_name = 'Blobby',
                        is_blob2 = True)
            blob2 = Blob(blue_blob_image,
                         blue_bullet_path,
                         blue_shield_path,
                         blue_dizzy_filepath,
                         surface,
                         bound.centerx-blob_height//2,
                         surface_height-blob_width,  
                         up =pygame.K_i,
                         down =pygame.K_k,
                         left =pygame.K_j, 
                         right =pygame.K_l,
                         shield_key = pygame.K_u, 
                         speed_boost_key =pygame.K_o, 
                         shoot_key= pygame.K_p,
                         magnet_key=pygame.K_SEMICOLON,
                         player_name = 'Blobster',
                         is_blob2 = False)
            food = Food(surface_width, surface_height)
            menu.paused = False
            menu.restart = False
            hp_bar = HPBar(screen, 25, 585, blob.player_name, blob2.player_name)
            trap = Trap(surface_height, surface_width)
            frame_counter = 0

    elif hp_bar.game_over == True:
        hp_bar.game_over = menu.game_over_menu(screen, hp_bar.game_over, hp_bar.winner)      

        if hp_bar.game_over == False:
            blob = Blob(red_blob_image,
                        red_bullet_path,
                        red_shield_path,
                        red_dizzy_filepath,
                        surface, 
                        bound.centerx-blob_height//2, 
                        0, 
                        up = pygame.K_w, 
                        down = pygame.K_s, 
                        left = pygame.K_a, 
                        right = pygame.K_d,
                        shield_key = pygame.K_q, 
                        speed_boost_key = pygame.K_e,
                        shoot_key= pygame.K_r, 
                        magnet_key=pygame.K_f,
                        player_name = 'Blobby',
                        is_blob2 = True)
            blob2 = Blob(blue_blob_image,
                         blue_bullet_path,
                         blue_shield_path,
                         blue_dizzy_filepath,
                         surface,
                         bound.centerx-blob_height//2,
                         surface_height-blob_width,  
                         up =pygame.K_i,
                         down =pygame.K_k,
                         left =pygame.K_j, 
                         right =pygame.K_l,
                         shield_key = pygame.K_u, 
                         speed_boost_key =pygame.K_o, 
                         shoot_key= pygame.K_p,
                         magnet_key=pygame.K_SEMICOLON,
                         player_name = 'Blobster',
                         is_blob2 = False)
            food = Food(surface_width, surface_height)
            hp_bar = HPBar(screen, 25, 585, blob.player_name, blob2.player_name)
            trap = Trap(surface_height, surface_width)
            frame_counter = 0

    else:     
        screen.blit(screen_background,(0,0))
        pygame.draw.rect(screen, outline_color, (20,20,560,560), 5)
        surface.blit(surface_background,(0,0))
        f_idx = food.draw(surface, blob.x, blob.y, blob2.x, blob2.y, blob.magnet_active, blob2.magnet_active)
        trap.draw(surface, frame_counter)
        blob.move()
        blob2.move()

        blob_eats = blob.eats_food(food.get_coordinates())
        if blob_eats:
            blob.update_score()
            if f_idx == food.speed_boost:
                blob.has_speed_boost += 1
            elif f_idx == food.shield:
                blob.has_shield += 1
            elif f_idx == food.magnet:
                blob.has_magnet += 1
            sound.play_eating_sound()
            food.get_food_pos()
             
        if blob.rect.collidepoint(trap.rect.center) and trap.trap_active:
            blob.trapped = True
            blob.apply_trap(frame_counter)
            trap.generate_position(frame_counter)
        blob2_eats = blob2.eats_food(food.get_coordinates())    
        if blob2_eats:
            blob2.update_score()
            if f_idx == food.speed_boost:
                blob2.has_speed_boost += 1
            elif f_idx == food.shield:
                blob2.has_shield += 1
            elif f_idx == food.magnet:
                blob2.has_magnet += 1 
            sound.play_eating_sound()
            food.get_food_pos()
            
        if blob2.rect.collidepoint(trap.rect.center) and trap.trap_active:
            blob2.trapped = True
            blob2.apply_trap(frame_counter)
            trap.generate_position(frame_counter)
            
        blob_hp_width, blob_hp_x, blob2_hp_width, blob2_hp_x = hp_bar.draw(frame_counter, blob_eats, blob2_eats)
           
        blob.apply_speed_boost(frame_counter)           
        blob.draw()
        blob.use_shield(frame_counter)
        blob.apply_shield(frame_counter)
        blob.use_speed_boost(frame_counter)
        blob.use_magnet(frame_counter)
        blob.apply_magnet(frame_counter)
        blob.remove_trap(frame_counter)
            
        blob2.apply_speed_boost(frame_counter)
        blob2.draw()
        blob2.use_shield(frame_counter)
        blob2.apply_shield(frame_counter) 
        blob2.use_speed_boost(frame_counter)  
        blob2.use_magnet(frame_counter)
        blob2.apply_magnet(frame_counter)  
        blob2.remove_trap(frame_counter)
            
        hp_bar.blob2_hp_width, hp_bar.blob2_hp_x, blob2.shield_active = blob.shoot_bullet(
            *blob.rect.center, *blob2.rect.center, frame_counter, blob2_hp_width, blob2_hp_x, 
            (blob2.rect.topleft[0]-15, blob2.rect.topleft[1]-20, 90, 90), blob2.shield_active)
        
        hp_bar.blob_hp_width, hp_bar.blob_hp_x, blob.shield_active = blob2.shoot_bullet(
            *blob2.rect.center, *blob.rect.center, frame_counter, blob_hp_width, blob_hp_x,
            (blob.rect.topleft[0]-15, blob.rect.topleft[1]-20, 90, 90), blob.shield_active)
        
        ability_bar.display(screen, blob.score, blob2.score, 25, 660, blob.has_shield, blob2.has_shield, 
                      blob.has_speed_boost, blob2.has_speed_boost, blob.has_magnet, blob2.has_magnet)
        
        screen.blits([(surface,(25,25))])
        pygame.display.update()