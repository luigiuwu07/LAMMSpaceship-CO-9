import pygame
import os

pygame.init()
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

RELOAD = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BULLET_POWER_UP = pygame.image.load(os.path.join(IMG_DIR, 'Other/powerUp.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

GAMEOVER_BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOverBack.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

#PowerUps types
DEFAULT_TYPE = 'default'
SHIELD_TYPE = 'shield'
SUPER_TYPE = 'super'

#objects types
SUPER_SPACESHIP_TYPE = 'super_spaceship'
ENEMY_TYPE = 'enemy'
SPACESHIP_TYPE = 'spaceship'

#Spaceships images
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SUPER_SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_power_up.png"))

#Bullets images
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
SUPER_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/super_bullet1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
#Enemies images
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
