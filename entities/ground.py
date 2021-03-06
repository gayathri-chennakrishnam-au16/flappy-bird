from entities.sprite import Sprite
import pathlib
import os
from util.constants import Constants
import pygame


class Ground(Sprite):
    def __init__(self):
        self.width = Constants.ground_width
        self.height = Constants.ground_height

        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path = os.path.join(current_path, "assets", "images", "ground.png")

        self.no_of_sprites = 2 * (Constants.width // self.width) + 2
        self.image = pygame.image.load(path)
        self.images = [self.image.get_rect()
                       for _ in range(self.no_of_sprites)]
        self.positions = list()
        self.draw_platform()

    def draw_platform(self):
        dx = 0
        for _ in range(self.no_of_sprites):
            x = self.width/2 + dx
            y = Constants.height - self.height / 2
            self.positions.append((x, y))
            dx += self.width

    def update_platform(self):
        speed = 1
        for idx in range(len(self.positions)):
            x, y = self.positions[idx]
            if x - speed <= -1 * Constants.width:
                self.positions[idx] = (
                    Constants.width + self.width / 2 - speed, y)
            else:
                self.positions[idx] = (x - speed, y)

    def display(self, screen):
        self.update_platform()
        for i in range(self.no_of_sprites):
            ground_rect = self.images[i]
            ground_rect.center = self.positions[i]
            screen.blit(self.image, ground_rect)
