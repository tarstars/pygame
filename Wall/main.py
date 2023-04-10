import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    img_torch = pygame.image.load(r"Images\torch_50.jpg")
    img_bricks = pygame.image.load(r"Images\bricks_50.jpg")
    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        screen.blit(img_torch,(10,10))
        for v in range()
        screen.blit(img_bricks, (60, 10))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
