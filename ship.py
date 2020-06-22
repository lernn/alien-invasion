import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx  = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right:
            if  self.rect.right > self.screen_rect.right:
                self.center = self.screen_rect.left
            else:
                self.center += self.ai_settings.ship_speed
        if self.moving_left:
            if self.rect.left < self.screen_rect.left:
                self.center = self.screen_rect.right
            else:
                self.center -= self.ai_settings.ship_speed
        self.rect.centerx = self.center


    def center_ship(self):
        self.center = self.screen_rect.centerx