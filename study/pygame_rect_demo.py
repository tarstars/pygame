import pygame


def draw_rectangles(screen, width, height):
    pygame.draw.rect(
        surface=screen,
        color=(255, 0, 0),
        rect=((100, 100), (100, 50))
    )

    pygame.draw.rect(
        surface=screen,
        color=(0, 0, 255),
        rect=((100, 300), (100, 100))
    )


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

        draw_rectangles(screen, width, height)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
