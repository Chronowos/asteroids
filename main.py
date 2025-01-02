import pygame
from constants import *
from player import Player

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatables in updatable:
            updatables.update(dt)

        screen.fill((0, 0, 0))

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()

        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()