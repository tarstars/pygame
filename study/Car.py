import pygame
import math


def circle_point(radius, center, n, point_number, omega, t):
    return center[0] + radius * math.cos(2 * math.pi / n * point_number + omega * t), center[1] + radius * math.sin(2 * math.pi / n * point_number + omega * t)


def draw_wheel(p0, t, screen):
        p1 = circle_point(center=p0, n=4, radius=70, point_number=0, omega=1, t=t)
        p2 = circle_point(center=p0, n=4, radius=70, point_number=1, omega=1, t=t)
        p3 = circle_point(center=p0, n=4, radius=70, point_number=2, omega=1, t=t)
        p4 = circle_point(center=p0, n=4, radius=70, point_number=3, omega=1, t=t)
        pygame.draw.circle(surface=screen, color=(250, 0, 0), center=p0, radius=70, width=2)
        pygame.draw.line(surface=screen, color=(0, 250, 0), start_pos=p1, end_pos=p3)
        pygame.draw.line(surface=screen, color=(0, 250, 0), start_pos=p2, end_pos=p4)


def draw_car(screen, t, pos):
    draw_wheel(p0=pos, t=t, screen=screen)
    draw_wheel(p0=(pos[0] + 150, pos[1]), t=t, screen=screen)


def main():
    t = 0
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
        t += 0.1
        draw_car(screen, t, pos=(200 + t * 100, 300))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
