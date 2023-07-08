import random

import pygame


def main():
    font = pygame.font.SysFont(None, 100)
    a = random.randint(1, 24)
    b = random.randint(1, 24)
    c = random.randint(1, 24)
    img_text_1 = font.render(f"{a}", True, (0, 0, 0))
    img_text_2 = font.render(f"{b}", True, (0, 0, 0))
    img_text_3 = font.render(f"{c}", True, (0, 0, 0))
    state = "green rect"
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
        screen.blit(img_text_1, (width // 2 - 100, height // 2))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
