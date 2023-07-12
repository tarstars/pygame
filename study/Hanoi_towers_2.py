import pygame


def main():
    a = [1, 2, 3, 4, 5, 6]
    y = 0
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
        for v in a:
            y += 50
            img_hanoi = pygame.image.load(f"../Images/Hanoi_{a[v]}.png")
            screen.blit(img_hanoi, (width // 2, height // 2 + y))
        y = 0
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
