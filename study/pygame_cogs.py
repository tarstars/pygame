import math

import pygame

# 10:47 - 


def circle_point(n, center_x, center_y, radius, t, omega, point_number):
    dphi = math.pi * 2 / n
    return (center_x + radius * math.cos(dphi * point_number + omega * t),
            center_y - radius * math.sin(dphi * point_number + omega * t))


def draw_cog(screen, n_teeth, color, center, radius, t, omega):
    for point_number in range(n_teeth):
        pygame.draw.circle(surface=screen,
                           color=color,
                           center=circle_point(n=n_teeth, center_x=center[0], center_y=center[1], radius=radius, t=t, 
                                               omega=omega,
                                               point_number=point_number),
                           radius=7
                           )


def two_cogs(screen, width, height, n_teeth, r_first, r_second, t):
    draw_cog(screen=screen, n_teeth=n_teeth, color=(255, 255, 0), center=(width // 2 - r_first, height // 2),
             radius=r_first, t=t, omega=2)
    draw_cog(screen=screen, n_teeth=n_teeth, color=(255, 255, 0), center=(width // 2 + r_second, height // 2),
             radius=r_second, t=t + math.pi / n_teeth / 2, omega=-1)


def main():
    shape = width, height = (1500, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    n_teeth = 32

    r_first = 150
    r_second = 300

    t = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        t += 0.005
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))

        two_cogs(screen, width, height, n_teeth, r_first, r_second, t)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
