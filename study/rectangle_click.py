import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    rect = pygame.Rect(200, 300, 50, 70)
    rectangle_state_on = True

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
                rectangle_state_on = not rectangle_state_on
        screen.fill((0, 170, 0))

        pygame.draw.rect(surface=screen, rect=rect, color=(0, 120, 0) if rectangle_state_on else (120, 0, 0))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
