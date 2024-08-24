from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(self, x , y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(velocity)    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
