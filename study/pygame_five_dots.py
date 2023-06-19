from math import cos, pi,  sin

import pygame

# 11:44 - 

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

        cx, cy = width // 2, height // 2
        for meter in range(5):
            phi = 2 * pi / 5 * meter
            x = cx + 200 * cos(phi)
            y = cy - 200 * sin(phi)
            pygame.draw.circle(surface=screen,
                               color=(255, 0, 0),
                               center=(x, y),
                               radius=10
                               )

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
