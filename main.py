import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfeild import AsteroidField

def main():
    #start the game
    pygame.init()
    # display window size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)

    Player.containers = (updatable, drawable)

    print("Starting asteroids!")
    # FPS starter
    clock = pygame.time.Clock()
    # dt variable
    dt = 0
    # main game loop
    
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 
        screen.fill((0, 0, 0))
        # moving player around
        for obj in updatable:
            obj.update(dt)
        # call player to loop
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        # FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()