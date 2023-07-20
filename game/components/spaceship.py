import pygame
from pygame.sprite import Sprite

from game.utils.constants import DEFAULT_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP, SPACESHIP_TYPE, SUPER_SPACESHIP_TYPE, SUPER_TYPE

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    SPACESHIP_HEIGHT = 60
    SPACESHIP_WIDTH = 50

    def __init__(self):
        self.type = SPACESHIP_TYPE
        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT] and user_input[pygame.K_UP]:
            self.move_topleft()
        elif user_input[pygame.K_RIGHT] and user_input[pygame.K_UP]:
            self.move_topright()
        elif user_input[pygame.K_LEFT] and user_input[pygame.K_DOWN]:
            self.move_bottomleft()
        elif user_input[pygame.K_RIGHT] and user_input[pygame.K_DOWN]:
            self.move_bottomright()
        elif user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_SPACE]:
            game.bullet_manager.add_bullet(self, game)
        

    def move_left(self):
        self.rect.x -= 10
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += 10
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = 0

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_topleft(self):
        if self.rect.left > 0 and self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.x -= 10
            self.rect.y -= 10

    def move_topright(self):
        if self.rect.right < SCREEN_WIDTH and self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.x += 10
            self.rect.y -= 10

    def move_bottomleft(self):
        if self.rect.left > 0 and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.x -= 10
            self.rect.y += 10

    def move_bottomright(self):
        if self.rect.right < SCREEN_WIDTH and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.x += 10
            self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def on_pick_power_up(self, time_up, type, image):
        self.image = pygame.transform.scale(image, (self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
        self.power_up_time_up = time_up
        self.power_up_type = type
        if self.power_up_type == SUPER_TYPE:
            self.type = SUPER_SPACESHIP_TYPE
            
    def draw_power_up(self,game):
        if game.shield_status == 3:
            self.power_up_type = DEFAULT_TYPE
            self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
            game.shield_status = 0
        if game.super_shoots == 5:
            self.type = SPACESHIP_TYPE
            self.power_up_type = DEFAULT_TYPE
            self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
            game.super_shoots = 0

        #if self.power_up_time_up != DEFAULT_TYPE:
        #    time_left = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
        #    if time_left == 0:
        #        self.power_up_type = DEFAULT_TYPE
        #        self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))
            #if time_left >= 0:
            #    game.menu.draw(game.screen, f"{self.power_up_type.capitalize()} is enable for {time_left} seconds", color=(255,255,255))
            #else:
            #    self.power_up_type = DEFAULT_TYPE
            #    self.image = pygame.transform.scale(SPACESHIP, (self.SPACESHIP_HEIGHT, self.SPACESHIP_WIDTH))