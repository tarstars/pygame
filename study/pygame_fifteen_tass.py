import pygame
import random

def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    numbers = [pygame.image.load(f"../Numbers/{v}.jpg") for v in range(1, 16)]
    click_sound = pygame.mixer.Sound("../Sounds/metal-short-tick.aiff")
    fart_sound = pygame.mixer.Sound("../Sounds/fart.mp3")
    font = pygame.font.SysFont(None, 400)
    img_win = font.render('WIN', True, (127, 0, 0))

    '''    field = [[14, 1, 2, 3],
                 [4, None, 6, 7],
                 [8, 9, 10, 11],
                 [12, 13, 0, 5]]'''

    field = [[0, 1, 2, 3],
                    [4, 5, 6, 7],
                    [8, 9, 10, 11],
                    [12, 13, None, 14]]

    field_solved = [[0, 1, 2, 3],
                 [4, 5, 6, 7],
                 [8, 9, 10, 11],
                 [12, 13, 14, None]]

    state = "game"

    hole_x, hole_y = 2, 3

    clock = pygame.time.Clock()
    while running:
        clock.tick(10)
        hole_next_x, hole_next_y = hole_x, hole_y
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hole_next_x -= 1
                elif event.key == pygame.K_RIGHT:
                    hole_next_x += 1
                elif event.key == pygame.K_UP:
                    hole_next_y -= 1
                elif event.key == pygame.K_DOWN:
                    hole_next_y += 1

        if (hole_x, hole_y) != (hole_next_x, hole_next_y):
            if 0 <= hole_next_x < 4 and 0 <= hole_next_y < 4:
                field[hole_y][hole_x], field[hole_next_y][hole_next_x] = field[hole_next_y][hole_next_x], field[hole_y][hole_x]
                if field == field_solved:
                    state = "win"
                hole_x, hole_y = hole_next_x, hole_next_y
                pygame.mixer.Sound.play(click_sound)
            else:
                pygame.mixer.Sound.play(fart_sound)

        screen.fill((0, 170, 0))

        if state == "game":
            for x in range(4):
                for y in range(4):
                    v = field[y][x]
                    if v is not None:
                        screen.blit(numbers[v], (width // 2 + 100 * (x - 2), height // 2 + 100 * (y - 2)))
        elif state == "win":
            for current_number in numbers:
                screen.blit(current_number, (random.randint(0, width), random.randint(0, height)))
            screen.blit(img_win, (width // 2 - img_win.get_width() // 2, height // 2 - img_win.get_height() // 2))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
