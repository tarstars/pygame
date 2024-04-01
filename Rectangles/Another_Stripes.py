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
        for y in range(0, 1000, 100):
            pygame.draw.rect(screen, (250, 0, 0), ((0, y), (width, 50)))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
