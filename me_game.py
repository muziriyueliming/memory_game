import sys
import pygame

class MemoryGame:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化资源并创建游戏资源。"""
        pygame.init()
        # self.settings = Settings()
        #制定大小模式
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Memory Game - 记忆力训练游戏。")
        self.bg_color = (0, 200, 50)
       
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    mg = MemoryGame()
    mg.run_game()

