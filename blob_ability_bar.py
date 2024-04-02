import pygame
from params import *

class AbilityBar:
    def __init__(self, player_name1, player_name2,shield_key1,shield_key2, 
                 speed_boost_key1, speed_boost_key2, bullet_key1, bullet_key2,
                 magnet_key1,magnet_key2):
        self.font = pygame.font.SysFont('tahoma', 15, True)
        self.font2 = pygame.font.SysFont('tahoma', 20, True)
        self.font3 = pygame.font.SysFont('tahoma', 15, True, True)
        self.blob_name1 = self.font.render(player_name1, True, (97, 19, 19))
        self.blob_name2 = self.font.render(player_name2, True, (22, 19, 97))
        
        self.red_blob = pygame.image.load(red_blob_angry_image).convert_alpha()
        self.red_blob = pygame.transform.scale(self.red_blob, (200, 150))

        self.blue_blob = pygame.image.load(blue_blob_angry_image).convert_alpha()
        self.blue_blob = pygame.transform.scale(self.blue_blob, (200, 150))
        
        self.shield_image = pygame.image.load(shield_image)
        self.shield_image = pygame.transform.scale(self.shield_image, (40, 40))
        self.shield1 = pygame.Rect(95-70, 585+35, 40, 40)
        self.shield2 = pygame.Rect(470+70, 585+35, 40, 40)
        self.shield_key_text1 = self.font3.render(f'{pygame.key.name(shield_key1)}', True, (97, 19, 19))
        self.shield_key_text2 = self.font3.render(f'{pygame.key.name(shield_key2)}', True, (22, 19, 97))

        self.speed_boost_image = pygame.image.load(speed_icon)
        self.speed_boost_image = pygame.transform.scale(self.speed_boost_image, (40, 40))
        self.speed_boost1 = pygame.Rect(95+45-70, 585+35, 40, 40)
        self.speed_boost2 = pygame.Rect(470-45+70, 585+35, 40, 40)
        self.speed_boost_key_text1 = self.font3.render(f'{pygame.key.name(speed_boost_key1)}', True, (97, 19, 19))
        self.speed_boost_key_text2 = self.font3.render(f'{pygame.key.name(speed_boost_key2)}', True, (22, 19, 97))

        self.bullet_image = pygame.image.load(bullet_icon)
        self.bullet_image = pygame.transform.scale(self.bullet_image, (40, 40))
        self.bullet1 = pygame.Rect(95+45+45-70, 585+35, 40, 40)
        self.bullet2 = pygame.Rect(470-45-45+70, 585+35, 40, 40)
        self.bullet_key_text1 = self.font3.render(f'{pygame.key.name(bullet_key1)}', True, (97, 19, 19))
        self.bullet_key_text2 = self.font3.render(f'{pygame.key.name(bullet_key2)}', True, (22, 19, 97))

        self.magnet_image = pygame.image.load(magnet_icon)
        self.magnet_image = pygame.transform.scale(self.magnet_image, (40, 40))
        self.magnet1 = pygame.Rect(95+45+45+45-70, 585+35, 40, 40)
        self.magnet2 = pygame.Rect(470-45-45-45+70, 585+35, 40, 40)
        self.magnet_key_text1 = self.font3.render(f'{pygame.key.name(magnet_key1)}', True, (97, 19, 19))
        self.magnet_key_text2 = self.font3.render(f'{pygame.key.name(magnet_key2)}', True, (22, 19, 97))


    def display(self, screen, score1, score2, x, y, has_shield1, has_shield2,
                has_speed_boost1, has_speed_boost2,has_magnet1, has_magnet2 ):
        self.score_text1 = self.font.render(f'Score: {score1}', True, (97, 19, 19))
        screen.blit(self.red_blob, (x + 60, y-70+30))
        
        self.score_text2 = self.font.render(f'Score: {score2}', True, (22, 19, 97))
        screen.blit(self.blue_blob, (x + 325 - 60, y-70+30))
        
        self.display_shield(screen, has_shield1, self.shield1, self.shield_key_text1,(97, 19, 19))
        self.display_shield(screen, has_shield2, self.shield2, self.shield_key_text2,(22, 19, 97))
       
        self.display_speed_boost( screen, has_speed_boost1, self.speed_boost1, self.speed_boost_key_text1,(97, 19, 19))
        self.display_speed_boost( screen, has_speed_boost2, self.speed_boost2, self.speed_boost_key_text2,(22, 19, 97))
        
        self.display_bullets( screen, score1, self.bullet1, self.bullet_key_text1,(97, 19, 19))
        self.display_bullets( screen, score2, self.bullet2, self.bullet_key_text2,(22, 19, 97))
        
        self.display_magnet( screen, has_magnet1, self.magnet1, self.magnet_key_text1,(97, 19, 19))
        self.display_magnet( screen, has_magnet2, self.magnet2,  self.magnet_key_text2,(22, 19, 97))
        
    def display_shield(self, screen, has_shield, shield_rect, shield_key_text, color):
        shield_text = self.font2.render(f'{has_shield}', True, color)
        shield_text_xy = shield_text.get_rect(center=shield_rect.center)
        screen.blit(self.shield_image, shield_rect.topleft)
        screen.blit(shield_text, shield_text_xy)
        screen.blit(shield_key_text, (shield_text_xy[0]+15, shield_text_xy[1]+15))

    def display_speed_boost(self, screen, has_speed_boost, speed_boost_rect, speed_boost_key_text, color):
        speed_boost_text = self.font2.render(f'{has_speed_boost}', True, color)
        speed_boost_text_xy = speed_boost_text.get_rect(center=speed_boost_rect.center)
        screen.blit(self.speed_boost_image, speed_boost_rect.topleft)
        screen.blit(speed_boost_text, speed_boost_text_xy)
        screen.blit(speed_boost_key_text, (speed_boost_text_xy[0]+15, speed_boost_text_xy[1]+15))

    def display_bullets(self, screen, score, bullet_rect, bullet_key_text, color):
        bullet_text = self.font2.render(f'{score}', True, color)
        bullet_text_xy = bullet_text.get_rect(center=bullet_rect.center)
        screen.blit(self.bullet_image, bullet_rect.topleft)
        screen.blit(bullet_text, bullet_text_xy)
        screen.blit(bullet_key_text, (bullet_text_xy[0]+15, bullet_text_xy[1]+15))

    def display_magnet(self, screen, has_magnet, magnet_rect, magnet_key_text, color):
        magnet_text = self.font2.render(f'{has_magnet}', True, color)
        magnet_text_xy = magnet_text.get_rect(center=magnet_rect.center)
        screen.blit(self.magnet_image, magnet_rect.topleft)
        screen.blit(magnet_text, magnet_text_xy)
        screen.blit(magnet_key_text, (magnet_text_xy[0]+15, magnet_text_xy[1]+15))