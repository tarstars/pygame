import math
import pygame
import random


def draw_sun(screen, local_meter, y):
    n = 17
    r = 200
    pygame.draw.circle(surface=screen, color=(250, 250, 0), center=(local_meter, y), radius=100)


def draw_scene(screen, width, height, meter):
    local_meter = (meter * 5) % width
    pygame.draw.rect(surface=screen, color=(0, 0, 0), rect=(0, 0, 100, 70))

    draw_sun(screen, local_meter, 100)

    for _ in range(30):
        pygame.draw.arc(surface=screen, color=(0, 255, 255),
                        rect=(random.randint(10, width), random.randint(10, height), 70, 70), start_angle=0,
                        stop_angle=3.14,
                        width=3)
    for _ in range(30):
        pygame.draw.arc(surface=screen, color=(255, 255, 255),
                        rect=(random.randint(10, width), random.randint(10, height), 90, 80), start_angle=4.16,
                        stop_angle=3.14,
                        width=8)


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    clock = pygame.time.Clock()
    meter = 0
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 128, 255))
        draw_scene(screen, width, height, meter)
        meter += 1
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()