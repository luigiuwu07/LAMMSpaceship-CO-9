from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLET_POWER_UP, SUPER_SPACESHIP, SUPER_TYPE


class BulletPowerUp(PowerUp):
    def __init__(self):
        super().__init__(BULLET_POWER_UP, SUPER_TYPE, SUPER_SPACESHIP)   