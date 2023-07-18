import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30
    Y_POS = 500
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
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

    def shoot(self, bullet_manager, user_input, bullet):
        if user_input[pygame.K_SPACE]:
            bullet.owner == BULLET
            bullet_manager.add_bullet(self)

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))