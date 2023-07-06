import pygame


def shift(a, b):
    return a[0] + b[0], a[1] + b[1]


def draw_poly_car(screen, pos):
    a = [(0, 0), (10, -10), (20, -10), (20, -30),  (30, 10), (30, 0), (50, 0), (30, 20), (70, -10), (60, -10), (70, -10), (80, 0), (100, 0), (100, -30), (-10, - 30), (-10, 0)]
    pygame.draw.polygon(surface=screen, color=(250, 0, 0), points=[shift(point, (pos)) for point in a])


def draw_car(screen):
    a = [(0, 0), (10, -10), (20, -10), (30, 0), (50, 0), (60, -10), (70, -10), (80, 0), (100, 0), (100, -30), (-10, - 30), (-10, 0)]
    prev = a[-1]
    for current in a:
        pygame.draw.line(surface=screen, color=(250, 0, 0), start_pos=shift(prev, (200, 200)), end_pos=shift(current, (200, 200)))
        prev = current


def main():
    x = 100
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
        x += 5
        draw_poly_car(screen, (x, 300))
        if x > width:
            x = 0
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
