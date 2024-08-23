import pygame
from constants import *

def main():
    #start the game
    pygame.init()
    # display window size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # FPS starter
    clock = pygame.time.Clock()
    # dt variable
    dt = 0
    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        # FPS to 60
        return dt == clock.tick(60) / 1000

if __name__ == "__main__":
    main()