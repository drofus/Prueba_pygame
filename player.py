import pygame

class Player:
    def __init__(self):
        self.x = 400
        self.y = 550
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 50, 10))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed