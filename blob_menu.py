import pygame, os

class Menu():
    def __init__(self, screen):
        
        self.screen = screen
        self.stop = False
        self.pcolor, self.rcolor, self.qcolor = 82, 82, 82
        font = pygame.font.SysFont('tahoma', 30, True)
        self.x = self.screen.get_rect().centerx
        self.menu_open = pygame.mixer.music.load('blob_files\music\menu.mp3')
        self.menu_click = pygame.mixer.music.load('blob_files\music\click.mp3')
        
        self.pause_text = font.render('RESUME', True, (255,255,255))
        self.pause_rect = pygame.Rect(50,50,130,50)
        self.pause_rect.centerx = self.x
        self.pause_text_xy = self.pause_text.get_rect(center = self.pause_rect.center)
        
        self.restart_text = font.render('RESTART', True, (255,255,255))
        self.restart_rect = pygame.Rect(50,150,160,50)
        self.restart_rect.centerx = self.x 
        self.restart_text_xy = self.restart_text.get_rect(center = self.restart_rect.center)
        
        self.quit_text = font.render('QUIT', True, (255,255,255))
        self.quit_rect = pygame.Rect(50,250,110,50)
        self.quit_rect.centerx = self.x 
        self.quit_text_xy = self.quit_text.get_rect(center = self.quit_rect.center)
        
        self.sound_on = pygame.image.load('blob_files\musicon.png').convert_alpha()
        self.sound_on_xy = self.sound_on.get_rect()
        self.sound_on_xy.center = self.x-32, 350  
        
        self.sound_off = pygame.image.load('blob_files\musicoff.png').convert_alpha()
        self.sound_off_xy= self.sound_off.get_rect()
        self.sound_off_xy.center = self.x+32, 350 
    
    def pause(self):
        if self.stop is not self.stop:
            pygame.mixer.music.play()
        
    def call(self, screen, background, music_channel):     
        
        screen.blit(background, (0,0))
        resume = pygame.draw.rect(screen, self.pcolor, self.pause_rect)
        restart = pygame.draw.rect(screen, self.rcolor, self.restart_rect)
        quit = pygame.draw.rect(screen, self.qcolor, self.quit_rect)
        
        if resume.collidepoint(pygame.mouse.get_pos()):     
            self.pcolor = 78, 168, 50
            if pygame.mouse.get_pressed()[0]:
                self.stop = False
        else:
            self.pcolor = 82, 82, 82
        
        if restart.collidepoint(pygame.mouse.get_pos()):     
            self.rcolor = 78, 168, 50
        else:
            self.rcolor = 82, 82, 82
        
        if quit.collidepoint(pygame.mouse.get_pos()):     
            self.qcolor = 78, 168, 50
        else:
            self.qcolor = 82, 82, 82
                    
        if self.sound_off_xy.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (78, 168, 50), self.sound_off_xy)
            if pygame.mouse.get_pressed()[0]:
                music_channel.pause()
            
        if self.sound_on_xy.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (78, 168, 50), self.sound_on_xy)
            if pygame.mouse.get_pressed()[0]:
                music_channel.unpause()
        
        screen.blits([(self.pause_text, self.pause_text_xy), (self.restart_text, self.restart_text_xy), 
                      (self.quit_text, self.quit_text_xy), (self.sound_on, self.sound_on_xy), 
                      (self.sound_off, self.sound_off_xy)])

        pygame.display.update()
        

# class Menu():
#     def __init__(self, screen):
#         self.screen = screen
#         self.pause = False
        
#         self.color = 82, 82, 82
#         font = pygame.font.SysFont('tahoma', 30, True)
        
#         self.centerx = screen.get_rect().centerx
#         print(self.centerx)
#         self.pause_text = font.render('PAUSE', True, (255,255,255))
#         self.pause_rect = pygame.Rect(50,50,130,50)
#         self.pause_text_xy = self.pause_text.get_rect()
#         self.pause_text_xy.center = self.centerx
        
#         self.restart_text = font.render('RESTART', True, (255,255,255))
#         self.restart_rect = pygame.Rect(50,150,160,50)
#         self.restart_text_xy = self.restart_text.get_rect(center = self.centerx)
        
#         self.quit_text = font.render('QUIT', True, (255,255,255))
#         self.quit_rect = pygame.Rect(50,250,110,50)
#         self.quit_text_xy = self.quit_text.get_rect(center = self.centerx)
        
#         self.sound_on = pygame.image.load('blob_files\musicon.png').convert_alpha()
#         self.sound_off = pygame.image.load('blob_files\musicoff.png').convert_alpha()
        
        
#     def call(self, screen, background):     
        
#         screen.blit(background, (0,0))
#         p = pygame.draw.rect(screen, self.color, self.pause_rect)
#         r = pygame.draw.rect(screen, self.color, self.restart_rect)
#         q = pygame.draw.rect(screen, self.color, self.quit_rect)
#         screen.blits([(self.pause_text, self.pause_text_xy), (self.restart_text, self.restart_text_xy), 
#                       (self.quit_text, self.quit_text_xy), (self.sound_on, (self.centerx-32, 350),
#                                                             (self.sound_off, (self.centerx+32, 350)))])
#         pygame.display.update()
        
