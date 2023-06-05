import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    dx, dy = 10, 0
    cx, cy = width // 2, height // 2

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx, dy = -10, 0
                elif event.key == pygame.K_w:
                    dx, dy = 0, -10
                elif event.key == pygame.K_s:
                    dx, dy = 0, 10
                elif event.key == pygame.K_d:
                    dx, dy = 10, 0
        screen.fill((0, 170, 0))

        pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(cx, cy), radius=3)
        pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(cx + dx, cy + dy), radius=3)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
