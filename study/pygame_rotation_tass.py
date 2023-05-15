import math

import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    clock = pygame.time.Clock()
    t = 0
    while running:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 100))


        r = 200 + 150 * math.cos(t / 3)
        x = width // 2 + r * math.cos(t)
        y = height // 2 - r * math.sin(t)
        
        pygame.draw.circle(surface=screen, color=(255, 255, 0), center=(width // 2, height // 2), radius=r, width=1)
        pygame.draw.circle(surface=screen, color=(127, 127, 0), center=(x, y), radius=10)
        pygame.draw.line(surface=screen, color=(255, 0, 0), start_pos=(x, 0), end_pos=(x, height))
        pygame.draw.line(surface=screen, color=(0, 255, 0), start_pos=(0, y), end_pos=(width, y))
        
        t += 0.01

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
