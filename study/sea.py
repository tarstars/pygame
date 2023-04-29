import math
import pygame
import random


def draw_sun(screen, local_meter, y):
    n = 17
    r = 200

    cx, cy = local_meter, y
    color = (250, 250, 0)
    pygame.draw.circle(surface=screen, color=color, center=(cx, cy), radius=100)

    for angle_meter in range(n):
        phi = 2 * math.pi * angle_meter / n
        dx, dy = r * math.cos(phi), r * math.sin(phi)
        pygame.draw.line(surface=screen,
                         color=color,
                         start_pos=(cx, cy),
                         end_pos=(cx + dx, cy + dy),
                         width=5)


def draw_scene(screen, width, height, meter):
    local_meter = (meter * 5) % width
    pygame.draw.rect(surface=screen, color=(102, 178, 255), rect=(0, 0, width, height//3))

    draw_sun(screen, local_meter, 100)

    for _ in range(30):
        pygame.draw.arc(surface=screen, color=(0, 255, 255),
                        rect=(random.randint(10, width), random.randint(height//3, height), 70, 70), start_angle=0,
                        stop_angle=3.14,
                        width=3)
    for _ in range(30):
        pygame.draw.arc(surface=screen, color=(255, 255, 255),
                        rect=(random.randint(10, width), random.randint(height//3, height), 90, 80), start_angle=4.16,
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
        clock.tick(5)
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