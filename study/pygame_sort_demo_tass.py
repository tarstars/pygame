import pygame
import random


def get_x(width, q, n):
    return width * q // n


def draw_scene(width, height, a, n, screen):
    delta = 100
    max_h = max(a)
    for q in range(n):
        pygame.draw.rect(
            surface=screen,
            color=(0, 40, 0),
            rect=( (delta + get_x(width - 2 * delta, q, n),
                    height - a[q] * (height - 2 * delta) / max_h - delta),
                  ((width - 2 * delta) // n,
                  a[q] * (height - 2 * delta) / max_h) )
        )

def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    n = 20
    a = [*range(1, n + 1)]
    random.shuffle(a)

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 30))
        draw_scene(width, height, a, n, screen)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
