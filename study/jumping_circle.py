import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    center_x = width // 2
    center_y = height // 2
    state = 0

    clock = pygame.time.Clock()
    while running:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if state == 0:
                    state = 1
                    animation_x = center_x
                    animation_y = center_y
                    if event.key == pygame.K_UP:
                        center_y -= 100
                    elif event.key == pygame.K_DOWN:
                        center_y += 100
                    elif event.key == pygame.K_LEFT:
                        center_x -= 100
                    elif event.key == pygame.K_RIGHT:
                        center_x += 100
        screen.fill((0, 170, 0))
        if state == 0:
            pygame.draw.circle(surface=screen, color=(100, 0, 100), center=(center_x, center_y), radius=50)
        elif state == 1:
            if center_x == animation_x and center_y == animation_y:
                state = 0
            else:
                if center_x > animation_x:
                    animation_x += 1
                if center_x < animation_x:
                    animation_x -= 1
                if center_y > animation_y:
                    animation_y += 1
                if center_y < animation_y:
                    animation_y -= 1
            pygame.draw.circle(surface=screen, color=(100, 0, 100), center=(animation_x, animation_y), radius=50)
            pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(center_x, center_y), radius=10)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
