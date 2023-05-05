import pygame
from player import Player
from enemy import Enemy

def run_game(screen):
    clock = pygame.time.Clock()
    player = Player()
    enemies = [Enemy() for _ in range(5)]

    while True:
        screen.fill((0, 0, 0))
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update()
        for enemy in enemies:
            enemy.update()