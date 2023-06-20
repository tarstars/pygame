import pygame
import math


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True


    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))
        for r in range(5):
            pygame.draw.circle(surface=screen, color=(250, 0, 0), center=(600 + math.cos(2/5*math.pi*r) * 300, 400 + math.sin(2/5*math.pi*r) * 300), radius=10)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
