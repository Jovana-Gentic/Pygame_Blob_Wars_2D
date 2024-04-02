import pygame
from blob_sounds import Sounds
from params import *

class Menu:
    def __init__(self, screen, up1, left1, down1, right1, up2, left2, down2, right2):
        self.up1, self.left1, self.down1, self.right1 = up1, left1, down1, right1
        self.up2, self.left2, self.down2, self.right2 = up2, left2, down2, right2
        
        self.running = True
        self.paused = False
        self.restart = False
        
        self.pcolor = self.rcolor = self.qcolor = 82, 82, 82
        self.font = pygame.font.SysFont('tahoma', 30, True)

        self.x = screen.get_rect().centerx
                
        self.pause_text = self.font.render('RESUME', True, (255, 255, 255))
        self.pause_rect = pygame.Rect(50, 50, 130, 50)
        self.pause_rect.centerx = self.x
        self.pause_text_xy = self.pause_text.get_rect(center=self.pause_rect.center)
        
        self.restart_text = self.font.render('RESTART', True, (255, 255, 255))
        self.restart_rect = pygame.Rect(50, 150, 160, 50)
        self.restart_rect.centerx = self.x 
        self.restart_text_xy = self.restart_text.get_rect(center=self.restart_rect.center)
        
        self.quit_text = self.font.render('QUIT', True, (255, 255, 255))
        self.quit_rect = pygame.Rect(50, 250, 110, 50)
        self.quit_rect.centerx = self.x 
        self.quit_text_xy = self.quit_text.get_rect(center=self.quit_rect.center)
        
        self.sound_on = pygame.image.load(music_on_image).convert_alpha()
        self.sound_on_xy = self.sound_on.get_rect()
        self.sound_on_xy.center = self.x - 32, 350  
        
        self.sound_off = pygame.image.load(music_off_image).convert_alpha()
        self.sound_off_xy = self.sound_off.get_rect()
        self.sound_off_xy.center = self.x + 32, 350 
        
        self.red_blob = pygame.image.load(red_blob_image).convert_alpha()
        self.red_blob = pygame.transform.scale(self.red_blob, (300,210))
        self.red_blob = pygame.transform.flip(self.red_blob, True, False)

        self.blue_blob = pygame.image.load(blue_blob_image).convert_alpha()
        self.blue_blob = pygame.transform.scale(self.blue_blob, (300,210))

        self.red_background = pygame.image.load(red_blob_background)
        self.blue_background = pygame.image.load(blue_blob_background)
        self.draw_background = pygame.image.load(draw_background)

        self.sound = Sounds()

    def call(self, screen, background, music_channel):
        screen.blit(background, (0,0))
    
        resume = pygame.draw.rect(screen, self.pcolor, self.pause_rect)
        restart = pygame.draw.rect(screen, self.rcolor, self.restart_rect)
        quit = pygame.draw.rect(screen, self.qcolor, self.quit_rect)
        
        if resume.collidepoint(pygame.mouse.get_pos()):
            self.pcolor = (78, 168, 50)
            if pygame.mouse.get_pressed()[0]:
                self.paused = False
                self.sound.play_menu_sound()
        else:
            self.pcolor = (82, 82, 82)
        
        if restart.collidepoint(pygame.mouse.get_pos()):
            self.rcolor = (78, 168, 50)
            if pygame.mouse.get_pressed()[0]:
                self.sound.play_menu_sound()
                self.restart = True
        else:
            self.rcolor = (82, 82, 82)
            
        if quit.collidepoint(pygame.mouse.get_pos()):
            self.qcolor = (78, 168, 50)
            if pygame.mouse.get_pressed()[0]:
                self.sound.play_menu_sound()
                self.running = False
        else:
            self.qcolor = (82, 82, 82)
        
        if self.sound_off_xy.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (78, 168, 50), self.sound_off_xy)
            if pygame.mouse.get_pressed()[0]:
                music_channel.pause()
        elif self.sound_on_xy.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (78, 168, 50), self.sound_on_xy)
            if pygame.mouse.get_pressed()[0]:
                music_channel.unpause()
            
        screen.blits([(self.pause_text, self.pause_text_xy), 
                    (self.restart_text, self.restart_text_xy), 
                    (self.quit_text, self.quit_text_xy), 
                    (self.sound_on, self.sound_on_xy), 
                    (self.sound_off, self.sound_off_xy)])
        
        pygame.display.update()
        return self.running, self.restart, self.up1, self.left1, self.down1, self.right1, self.up2, self.left2, self.down2, self.right2

    def game_over_menu(self, screen, game_over, winner):
        if winner == 1:
            screen.blit(self.red_background, (0, 0), (18, 150, 600,700))
        elif winner ==2:
            screen.blit(self.blue_background, (0, 0), (18, 200, 600,700))
        else:
            screen.blit(self.draw_background, (0, 0), (18, 200, 600,700))
        game_over = game_over
        
        restart = pygame.draw.rect(screen, self.rcolor, self.restart_rect)
        if restart.collidepoint(pygame.mouse.get_pos()):
            self.rcolor = (78, 168, 50)
            if pygame.mouse.get_pressed()[0]:
                self.sound.play_menu_sound()
                self.restart = True
                game_over = False
        else:
            self.rcolor = (82, 82, 82)
            
        screen.blit(self.restart_text, self.restart_text_xy)
        pygame.display.update()
        return game_over