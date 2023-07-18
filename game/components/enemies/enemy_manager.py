from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        if not self.enemies:
            self.enemies.append(Enemy())

        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)