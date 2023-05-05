import pygame
import sys
from menu import show_menu
from game import run_game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Game")

    while True:
        choice = show_menu(screen)
        if choice == "play":
            run_game(screen)
        elif choice == "quit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()