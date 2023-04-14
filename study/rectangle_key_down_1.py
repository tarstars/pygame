import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    rect = pygame.Rect(120, 300, 100, 100)
    rectangle_state_on = True

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    rectangle_state_on = not rectangle_state_on
        screen.fill((0, 170, 0))

        pygame.draw.arc(surface=screen, rect=rect, color=(120, 0, 120) if rectangle_state_on else (120, 120, 50), start_angle=12, stop_angle=50, width=100)
        # pygame.display.update()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
