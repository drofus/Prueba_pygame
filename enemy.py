import pygame
import random

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 750)
        self.y = random.randint(50, 200)
        self.speed = 2

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 30, 30))

    def update(self):
        self.y += self.speed
        if self.y > 600:
            self.y = 0
            self.x = random.randint(0, 750)