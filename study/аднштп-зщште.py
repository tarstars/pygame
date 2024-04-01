import pygame
import math



def circle_point(radius, center, n, point_number, omega, t):
    return center[0] + radius * math.cos(2 * math.pi / n * point_number + omega * t), center[1] + radius * math.sin(2 * math.pi / n * point_number + omega * t)



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
        p0 = (width // 2, height // 2)
        p1 = circle_point(center=p0, n=7, point_number=0, omega=0.5, t=t, radius=100)
        pygame.draw.circle(surface=screen, center=p1, color=(250, 0, 0), radius=10)
        p2 = circle_point(center=p1, n=7, point_number=0, omega=1, t=t, radius=50)
        pygame.draw.circle(surface=screen, center=p2, color=(250, 0, 0), radius=10)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()