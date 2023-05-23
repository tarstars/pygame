import pygame


def draw_scene(screen, width, height):
    r = min(width // 2, height // 2)
    for p in range(0, r, 10):
        pygame.draw.aaline(screen, (255, 255, 0), (width // 2, height // 2 - r + p), (width // 2 + p, height // 2))
        pygame.draw.aaline(screen, (255, 255, 0), (width // 2, height // 2 + r - p), (width // 2 - p, height // 2))
        pygame.draw.aaline(screen, (255, 255, 0), (width // 2, height // 2 - r + p), (width // 2 - p, height // 2))
        pygame.draw.aaline(screen, (255, 255, 0), (width // 2, height // 2 + r - p), (width // 2 + p, height // 2))


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
