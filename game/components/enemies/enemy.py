import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1,ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = "left"
RIGHT = "right"
class Enemy(Sprite):
    X_POS_LIST = [i for i in range(50, SCREEN_WIDTH, 50)]
    Y_POS = 20
    SPEED_X = 5
    ENEMY_TYPES = [ENEMY_1,ENEMY_2]
    def __init__(self):
        self.current_enemy = random.choice(self.ENEMY_TYPES)
        self.image = pygame.transform.scale(self.current_enemy, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS

        self.speed_x = self.SPEED_X
        self.speed_y = 1 if self.current_enemy==ENEMY_1 else 10
        self.movement = random.choice([LEFT,RIGHT])
        self.move_x = random.randint(30,100)
        self.moving_index = 0

    def update(self, enemies):
        self.rect.y += self.speed_y
        if self.movement == RIGHT:
            self.rect.x += self.speed_x
        else:
            self.rect.x -= self.speed_x
        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            enemies.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.right >= SCREEN_WIDTH:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))