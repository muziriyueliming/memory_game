import pygame

class Pictrue:
    """管理图片的类。"""

    def __init__(self, mg_game):
        """初始化并设置其初始位置。"""
        self.screen = mg_game.screen
        self.screen_rect = mg_game.screen.get_rect()

        #加载图像并获取其外接矩形
        # ims = ["images/0.jpg","images/01.jpg"]
        
    def blitme(self):
        """在指定位置绘制照片。"""
        ims = {
            '0' : 'images/0.jpg',
            '1' : 'images/1.jpeg',
            '2' : 'images/2.jpeg',
            }

        for k, v in ims.items():
            v = '' + v
            self.image = pygame.image.load(v)
            self.rect = self.image.get_rect()

            #对于每艘新飞船，都将其放在屏幕底部的中央。
            self.rect.left = self.screen_rect.left + 20 + (20 + self.rect.width) * int(k)
            self.rect.top = self.screen_rect.top +20

            self.screen.blit(self.image, self.rect)
