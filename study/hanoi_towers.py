import random

import pygame


def main():
    a = [1, 2, 3, 4, 5, 6]
    b = []
    c = []
    img_green_rect = pygame.image.load("../Images/green_rect.png")
    img_red_rect = pygame.image.load("../Images/red_rect.png")
    chosen_1 = 0
    chosen_2 = 0
    m = [a, b, c]
    state = "green rect"
    shape = width, height = (1200, 800)
    pygame.init()
    font = pygame.font.SysFont(None, 100)
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
                        arr_from = m[chosen_1]
                        arr_to = m[chosen_2]
                        disc = arr_from.pop()
                        arr_to.append(disc)
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
        y = 0
        for v in m[0]:
            y -= 50
            img_hanoi = pygame.image.load(f"../Images/Hanoi_{v}.png")
            screen.blit(img_hanoi, (width // 2, height // 2 + y))
        y = 0
        for v in m[1]:
            y -= 50
            img_hanoi = pygame.image.load(f"../Images/Hanoi_{v}.png")
            screen.blit(img_hanoi, (width // 2 - 300, height // 2 + y))
        y = 0
        for v in m[2]:
            y -= 50
            img_hanoi = pygame.image.load(f"../Images/Hanoi_{v}.png")
            screen.blit(img_hanoi, (width // 2 - 600, height // 2 + y))
        y = 0
        x1 = width // 2 - 400 + chosen_1 * 300
        x2 = width // 2 - 400 + chosen_2 * 300
        y = height // 2 - 100
        screen.blit(img_green_rect, (x1, y))
        if state == "red rect":
            screen.blit(img_red_rect, (x2, y))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()