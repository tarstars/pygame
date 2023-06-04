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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("a")
                elif event.key == pygame.K_w:
                    print("w")
                elif event.key == pygame.K_s:
                    print("s")
                elif event.key == pygame.K_d:
                    print("d")
        screen.fill((0, 170, 0))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
