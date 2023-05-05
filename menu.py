import pygame

def show_menu(screen):
    font = pygame.font.Font(None, 36)
    play_text = font.render("Play", True, (255, 255, 255))
    quit_text = font.render("Quit", True, (255, 255, 255))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(play_text, (350, 250))
        screen.blit(quit_text, (350, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 350 <= x <= 350 + play_text.get_width() and 250 <= y <= 250 + play_text.get_height():
                    return "play"
                elif 350 <= x <= 350 + quit_text.get_width() and 300 <= y <= 300 + quit_text.get_height():
                    return "quit"