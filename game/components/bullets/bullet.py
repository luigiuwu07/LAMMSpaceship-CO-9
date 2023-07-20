import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, SCREEN_HEIGHT, SPACESHIP_TYPE, SUPER_BULLET, SUPER_SPACESHIP_TYPE

class Bullet:
    SPEED = 20
    BULLETS = {ENEMY_TYPE: BULLET_ENEMY,
               SPACESHIP_TYPE: BULLET,
               SUPER_SPACESHIP_TYPE: SUPER_BULLET}

    def __init__(self, spaceship):
        self.owner = spaceship.type
        if self.owner == SUPER_SPACESHIP_TYPE:
            self.image = pygame.transform.scale(self.BULLETS[self.owner],(60,50))
        else:
            self.image = pygame.transform.scale(self.BULLETS[self.owner],(10,30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
        else:
            self.rect.y -= self.SPEED
            
        if self.rect.y >= SCREEN_HEIGHT or self.rect.y <= 0:
                bullets.remove(self)

    def draw(self, screen):
        if self.owner == ENEMY_TYPE:
            screen.blit(self.image, self.rect)
        if self.owner == SPACESHIP_TYPE:
            screen.blit(self.image, self.rect)
        if self.owner == SUPER_SPACESHIP_TYPE:
            screen.blit(self.image, self.rect)