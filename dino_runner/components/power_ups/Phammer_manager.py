import random
import pygame

from dino_runner.components.power_ups.hammer import Hammer


class HammerManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score): # faz aparecer a teg
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(300, 400)
            self.power_ups.append(Hammer())

    def update(self, game): # o poder
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time =pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen): #o desenho
        for power_up in self.power_ups:
            power_up.draw(screen) 

    def reset_power_ups(self): # resert
        self.power_ups = []
        self.when_appears = random.randint(300, 400)