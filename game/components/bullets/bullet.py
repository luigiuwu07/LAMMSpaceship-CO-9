import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE,SPACESHIP_TYPE , SCREEN_HEIGHT

class Bullet:
    SPEED = 20
    BULLETS = {ENEMY_TYPE: BULLET_ENEMY,
               SPACESHIP_TYPE: BULLET}

    def __init__(self, spaceship):
        self.owner = spaceship.type
        self.image = pygame.transform.scale(self.BULLETS[self.owner],(10,30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        if self.owner == SPACESHIP_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y >= 0:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)