import pygame
import sys
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1280,800))
    bg_color = (190,100,100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run_game()