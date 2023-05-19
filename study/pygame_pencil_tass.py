import random

import pygame


def transform(img):
    return pygame.transform.scale(img, (50, 100))


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    n = random.randint(1, 20)
    img_pen = transform(pygame.image.load("../Pencils/red.jpg"))
    img_pen_sel = transform(pygame.image.load("../Pencils/red_selected.jpg"))
    state = "choice"
    n_selected = 1

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and n_selected < min(3, n):
                    n_selected += 1
                elif event.key == pygame.K_RIGHT and n_selected > 1:
                    n_selected -= 1
                elif event.key == pygame.K_SPACE:
                    n -= n_selected

        screen.fill((0, 170, 0))

        for q in range(n):
            screen.blit(img_pen if q < n - n_selected else img_pen_sel, (10 + q*(img_pen.get_width() + 10), 
                                                                         (height - img_pen.get_height()) // 2))

        pygame.display.update()
        if n == 0:
            running = False
    pygame.quit()


if __name__ == "__main__":
    main()
