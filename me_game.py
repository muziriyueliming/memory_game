import sys
import pygame
from settings import Settings
from pictrue import Pictrue 

class MemoryGame:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化资源并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Memory Game - 记忆力训练游戏。")
        self.pictrue = Pictrue(self)
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.pictrue.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    mg = MemoryGame()
    mg.run_game()

