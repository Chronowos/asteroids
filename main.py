import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (shoots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatables in updatable:
            updatables.update(dt)

        for aster in asteroids:
            if aster.check_collision(player):
                print("Game over")
                return
            
            for bullet in shoots:
                if bullet.check_collision(aster):
                     bullet.kill()
                     aster.split()


        screen.fill((0, 0, 0))

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()

        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()