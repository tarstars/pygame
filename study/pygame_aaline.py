import pygame


def draw_scene(screen, width, height):
    for p in range(0, 400, 10):
        pygame.draw.aaline(screen, (255, 255, 0), (200, 200 + p), (200 + p, 600))


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
        screen.fill((0, 0, 255))
        draw_scene(screen, width, height)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
