import pygame

class HPBar:
    def __init__(self, screen, x, y, text, text2):
        self.screen = screen
        self.outline_width, self.outline_height = 180, 30
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        font = pygame.font.SysFont('tahoma', 20, True)
        self.x = x
        self.y = y
        
        self.text = text
        self.text_surface = font.render(self.text, True, self.BLACK)
        self.blob_hp_x = x
        self.blob_hp_y = y
        self.score1 = 0
        self.blob_hp_width = 180
        self.blob_hp_height = 30
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topleft = (self.blob_hp_x + 5, self.blob_hp_y + (self.outline_height - self.text_rect.height) // 2)
       
        self.text2 = text2
        self.text_surface2 = font.render(self.text2, True, self.BLACK)
        self.blob2_hp_x = x
        self.blob2_hp_y = y
        self.score2 = 0
        self.blob2_hp_width = 180
        self.blob2_hp_height = 30
        self.text_rect2 = self.text_surface.get_rect()
        self.text_rect2.topright = (self.x+525 + self.outline_height - 5, self.y + (self.outline_height - self.text_rect2.height) // 2)
        text_width = self.text_surface2.get_width()
        self.text_rect2.right = self.x + 525 + self.outline_height - 5
        self.text_rect2.left = self.text_rect2.right - text_width
        
        self.game_over = False
        self.winner = 0
        
    def draw(self, frame_counter, blob_eats, blob2_eats):
        if (frame_counter % 20) == 0:
            self.blob_hp_width -= 1
            self.blob2_hp_width -=1
            self.blob2_hp_x += 1
            
        if blob_eats:
            self.blob_hp_width = min(self.blob_hp_width+20, 180)
            
        if blob2_eats:
            self.blob2_hp_width = min(self.blob2_hp_width+20, 180)
            self.blob2_hp_x = max(self.blob2_hp_x-20, self.x)
            
        if (self.blob_hp_width == 0) or (self.blob2_hp_width == 0):
            if (self.blob_hp_width == 0) and (self.blob2_hp_width > 0):
                self.game_over = True
                self.winner = 2
            elif (self.blob2_hp_width == 0) and (self.blob_hp_width > 0):
                self.game_over = True
                self.winner = 1
            else:
                self.game_over = True
                self.winner = 3

        pygame.draw.rect(self.screen, self.BLACK, (self.blob_hp_x-2, self.blob2_hp_y-2, self.outline_width+2, self.outline_height+4), 3)
        pygame.draw.rect(self.screen, self.GREEN, (self.blob_hp_x + 1, self.blob_hp_y + 1, self.blob_hp_width - 2, self.blob_hp_height - 2))
        self.screen.blit(self.text_surface, self.text_rect)
        
        pygame.draw.rect(self.screen, self.BLACK, (self.x+370-2, self.y-2, self.outline_width+4, self.outline_height+4), 3)
        pygame.draw.rect(self.screen, self.GREEN, (self.blob2_hp_x+370 + 1, self.blob2_hp_y + 1, self.blob2_hp_width - 2, self.blob2_hp_height - 2))
        self.screen.blit(self.text_surface2, self.text_rect2)
        
        return self.blob_hp_width, self.blob_hp_x, self.blob2_hp_width, self.blob2_hp_x