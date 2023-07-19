import pygame
from game.components.menu import Menu


class GameOverMenu(Menu):
    def __init__(self, message, game):
        super().__init__(message)
        self.update_score(game.score)
        self.update_max_score(game.max_score)
        self.update_death_count(game.death_count)

    def draw(self, screen):
        super()
        screen.blit(self.text1, self.text1_rect)
        screen.blit(self.text2, self.text2_rect)
        screen.blit(self.text3, self.text3_rect)
        pygame.display.flip()

    def update_message(self, message):
        return super().update_message(message)

    def update_score(self, score):
        self.Score = score
        self.text1 = self.font.render(str(self.Score), True, (255,0,0))
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 30)

    def update_max_score(self, max_score):
        self.Max_score = max_score
        self.text2 = self.font.render(str(self.Max_score), True, (255,0,0))
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update_death_count(self, death_count):
        self.Death_count = death_count
        self.text3 = self.font.render(str(self.Death_count), True, (255,0,0))
        self.text3_rect = self.text3.get_rect()
        self.text3_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 30)