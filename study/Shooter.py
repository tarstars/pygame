import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    dx = 20
    dy = 0
    x = 0
    y = 0
    pew_sound = pygame.mixer.Sound("../Sounds/a8887ebd8bd4435.mp3")

    clock = pygame.time.Clock()
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx = -20
                    dy = 0
                elif event.key == pygame.K_w:
                    dx = 0
                    dy = -20
                elif event.key == pygame.K_s:
                    dx = 0
                    dy = 20
                elif event.key == pygame.K_d:
                    dx = 20
                    dy = 0
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(pew_sound)
        x, y = x + dx, y + dy
        screen.fill((0, 170, 0))
        pygame.draw.circle(screen, (250, 0, 0), (width // 2 + x, height // 2 + y), 5)
        pygame.draw.circle(screen, (250, 0, 0), (width // 2 + x, height // 2 + y - 10), 5)
        pygame.draw.circle(screen, (250, 0, 0), (width // 2 + x, height // 2 + y + 10), 5)
        pygame.draw.circle(screen, (250, 0, 0), (width // 2 + x - 10, height // 2 + y), 5)
        pygame.draw.circle(screen, (250, 0, 0), (width // 2 + x + 10, height // 2 + y), 5)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
