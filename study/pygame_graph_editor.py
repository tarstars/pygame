import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    x, y = width // 2, height // 2
    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 4
        elif keys[pygame.K_RIGHT]:
            x += 4
        elif keys[pygame.K_UP]:
            y -= 4
        elif keys[pygame.K_DOWN]:
            y += 4

        screen.fill((0, 170, 0))
        pygame.draw.line(screen, (255, 255, 8), (x - 10, y), (x + 10, y))
        pygame.draw.line(screen, (255, 255, 8), (x, y - 10), (x, y + 10))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
