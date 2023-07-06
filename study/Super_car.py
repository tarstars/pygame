import pygame


def main():
    x = 100
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    img_car = pygame.image.load("../Images/Super_car.png")
    running = True

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))
        screen.blit(img_car, (x, height // 2))
        x += 5
        if x > width:
            x = 0
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
