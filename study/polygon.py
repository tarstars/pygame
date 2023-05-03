import pygame


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
        pygame.draw.circle(surface=screen, color=(0, 128, 255), center=(400, 300), radius=100, width=100)
        pygame.draw.polygon(surface=screen, color=(250, 0, 250), points=((600, 400), (700, 400), (700, 500), (600, 500)))
        pygame.draw.polygon(surface=screen, color=(250, 0, 250),
                            points=((700, 500), (650, 600), (600, 500)))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()