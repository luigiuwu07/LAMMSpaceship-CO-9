import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies import enemy_manager

from game.components.enemies.enemy_manager import EnemyManager
from game.components.game_over_menu import GameOverMenu
from game.components.menu import Menu
from game.components.spaceship import Spaceship

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu("Press ENTER to start.")
        self.score = 0
        self.max_score = 0
        self.death_count = 0
        self.game_over_menu = GameOverMenu("Game Over", self)

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                #self.show_game_over()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.playing = True
        self.enemy_manager.reset()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_close()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self, self.enemy_manager.enemies)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        if self.death_count > 0:
            if self.score > self.max_score:
                self.max_score = self.score
            self.game_over_menu.update_max_score(f"Max score: {self.max_score}")
            self.game_over_menu.update_score(f"Score: {self.score}")
            self.game_over_menu.update_death_count(f"Deads: {self.death_count}")
            self.game_over_menu.draw(self.screen)
            self.game_over_menu.events(self.on_close, self.play)
        else:
            self.menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False
"""
    def show_game_over(self):
        #if self.death_count > 0:
        if self.score > self.max_score:
            self.max_score = self.score
        self.game_over_menu.draw(self.screen)
        self.game_over_menu.update_death_count(f"Score: {self.death_count}")
        self.game_over_menu.update_score(f"Score: {self.score}")
        self.game_over_menu.update_max_score(f"Score: {self.max_score}")
"""