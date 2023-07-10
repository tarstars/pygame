import random

import pygame


def main():
    img_green_rect = pygame.image.load("../Images/green_rect.png")
    img_red_rect = pygame.image.load("../Images/red_rect.png")
    chosen_1 = 0
    chosen_2 = 0
    a = random.randint(1, 24)
    b = random.randint(1, 24)
    c = random.randint(1, 24)
    state = "green rect"
    shape = width, height = (1200, 800)
    pygame.init()
    font = pygame.font.SysFont(None, 100)
    img_text_1 = font.render(f"{a}", True, (0, 0, 0))
    img_text_2 = font.render(f"{b}", True, (0, 0, 0))
    img_text_3 = font.render(f"{c}", True, (0, 0, 0))
    screen = pygame.display.set_mode(shape)
    running = True

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if state == "green rect":
                        state = "red rect"
                    elif state == "red rect":
                        state = "green rect"
                elif event.key == pygame.K_a:
                    if state == "green rect":
                        if chosen_1 > 0:
                            chosen_1 -= 1
                    elif state == "red rect":
                        if chosen_2 > 0:
                            chosen_2 -= 1
                elif event.key == pygame.K_d:
                    if state == "green rect":
                        if chosen_1 < 2:
                            chosen_1 += 1
                    elif state == "red rect":
                        if chosen_2 < 2:
                            chosen_2 += 1
            if event.type == pygame.QUIT:
                running = False
        screen.fill((250, 50, 250))
        x = width // 2 - 100 + chosen_1 * 300
        y = height // 2 - 100
        screen.blit(img_text_1, (width // 2 - 300, height // 2))
        screen.blit(img_text_2, (width // 2, height // 2))
        screen.blit(img_text_3, (width // 2 + 300, height // 2))
        screen.blit(img_green_rect, (x, y))
        if state == "red rect":
            screen.blit(img_red_rect, (x + chosen_2 * 300, y))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
