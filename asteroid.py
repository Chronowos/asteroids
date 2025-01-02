import pygame
import random
import constants
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        velocity_new1 = self.velocity.rotate(random_angle)
        velocity_new2 = self.velocity.rotate(-random_angle)

        radius_new = self.radius - constants.ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, radius_new)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, radius_new)
        
        new_asteroid1.velocity = velocity_new1 * 1.2
        new_asteroid2.velocity = velocity_new2