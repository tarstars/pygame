import math

import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    t = 0
    r = 400

    clock = pygame.time.Clock()
    while running:
        t += 0.01
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))
        pygame.draw.circle(surface=screen, color=(255, 0, 0),
                           center=(width // 2, height // 2), radius=r, width=3)
        pygame.draw.circle(surface=screen, color=(255, 100, 255), center=(width // 2 + math.cos(t) * r, height // 2 + -math.sin(t) * r), radius=10)
        pygame.draw.aaline(surface=screen, color=(255, 255, 255), start_pos=(width // 2 + math.cos(t) * r, 0), end_pos=(width // 2 + math.cos(t) * r, height))
        pygame.draw.aaline(surface=screen, color=(255, 255, 255), start_pos=(0, height // 2 + -math.sin(t) * r), end_pos=(width, height // 2 + -math.sin(t) * r))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
