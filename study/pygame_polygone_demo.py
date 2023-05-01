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

        pygame.draw.polygon(screen, (255, 255, 0), [(600, 400), (600, 500), (700, 500), (700, 400), (710, 400), (650, 300), (590, 400)])

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
