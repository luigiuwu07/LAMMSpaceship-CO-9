import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SPACESHIP_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.spaceship_bullets = []

    def update(self, game, enemies):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.playing = False
                game.death_count += 1
                print(game.death_count)
                pygame.time.delay(1000)
                break
        for spaceship_bullet in self.spaceship_bullets:
            spaceship_bullet.update(self.spaceship_bullets)
            for enemy in enemies:
                if spaceship_bullet.rect.colliderect(enemy.rect):
                    self.spaceship_bullets.remove(spaceship_bullet)
                    enemies.remove(enemy)
                    game.score += 1
    
    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)
        for spaceship_bullet in self.spaceship_bullets:
            spaceship_bullet.draw(screen)

    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
        if spaceship.type == SPACESHIP_TYPE and len(self.spaceship_bullets) < 1:
            self.spaceship_bullets.append(Bullet(spaceship))