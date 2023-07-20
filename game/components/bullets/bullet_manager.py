import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, ENEMY_TYPE, SHIELD_TYPE, SPACESHIP_TYPE, SUPER_SPACESHIP_TYPE, SUPER_TYPE


class BulletManager:
    def __init__(self):
        self.enemy_bullets = []
        self.spaceship_bullets = []
        self.super_shoots = 0
        self.shoot_sound = pygame.mixer.Sound("game/assets/Music/blaster.wav")
        self.game_over_sound = pygame.mixer.Sound("game/assets/Music/game_over.wav")

    def update(self, game, enemies):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                if game.player.power_up_type == DEFAULT_TYPE or game.player.power_up_type == SUPER_TYPE:
                    pygame.mixer.music.stop()
                    self.game_over_sound.play()
                    game.playing = False
                    game.player.type = SPACESHIP_TYPE
                    game.death_count += 1
                    pygame.time.delay(1000)
                    break
                elif game.player.power_up_type == SHIELD_TYPE:
                    game.shield_status += 1
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

    def add_bullet(self, spaceship, game):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))

        if spaceship.type == SPACESHIP_TYPE and len(self.spaceship_bullets) < 1:
            self.spaceship_bullets.append(Bullet(spaceship))
            self.shoot_sound.play()
        
        if spaceship.type == SUPER_SPACESHIP_TYPE and len(self.spaceship_bullets) < 1:
            self.spaceship_bullets.append(Bullet(spaceship))
            game.super_shoots += 1
            self.shoot_sound.play()