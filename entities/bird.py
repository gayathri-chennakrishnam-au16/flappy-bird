from mechanics.collition_detector import CollitionDetector
from entities.sprite import Sprite
import os
import pathlib
from util.constants import Constants

import pygame


class Bird(Sprite):
    bird_frame = 0
    def __init__(self):
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path =  os.path.join(current_path, "assets", "images", "bird.png")
        self.image = pygame.image.load(path)
        self.bird_rect = self.image.get_rect()
        self.bird_rect.center = (400, 200)
        self.accelaration = 0

    def jump(self):
        self.accelaration = 0
        self.accelaration -= 2

    def animate(self):
        Bird.bird_frame = (Bird.bird_frame + 1) % 3
    
    def apply_gravity(self):
        gravity = 0.015
        self.accelaration += gravity

    def collition_detected(self, pipes):
        collition_detector = CollitionDetector()
        for pipe in pipes:
            if collition_detector.is_collided_with(self.bird_rect, pipe):
                return True

        if self.bird_rect.midbottom[1] >= Constants.height:
            return True

        if self.bird_rect.midtop[1] <= 0:
            return True
        return False

    def display(self, screen):
        self.bird_rect.centery += self.accelaration
        screen.blit(self.image, self.bird_rect, (Bird.bird_frame * Constants.bird_width, 0, Constants.bird_width, Constants.bird_height)) 
    
    
