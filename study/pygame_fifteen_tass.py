import copy

import pygame
import random


def find_hole(field):
    for p in range(len(field)):
        for q in range(len(field[0])):
            if field[p][q] is None:
                return q, p


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
    img_shuffle = font.render('shuffle', True, (127, 0, 0))

    field_solved = [[0, 1, 2, 3],
                 [4, 5, 6, 7],
                 [8, 9, 10, 11],
                 [12, 13, 14, None]]

    field = copy.deepcopy(field_solved)

    state = "shuffle"
    shuffle_meter = 300

    hole_x, hole_y = find_hole(field)

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        hole_next_x, hole_next_y = hole_x, hole_y

        my_key = None
        if state == "shuffle":
            my_key = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN][random.randint(0, 3)]
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    my_key = event.key

        if my_key == pygame.K_LEFT:
            hole_next_x -= 1
        elif my_key == pygame.K_RIGHT:
            hole_next_x += 1
        elif my_key == pygame.K_UP:
            hole_next_y -= 1
        elif my_key == pygame.K_DOWN:
            hole_next_y += 1

        if (hole_x, hole_y) != (hole_next_x, hole_next_y):
            if 0 <= hole_next_x < 4 and 0 <= hole_next_y < 4:
                field[hole_y][hole_x], field[hole_next_y][hole_next_x] = field[hole_next_y][hole_next_x], field[hole_y][hole_x]
                if field == field_solved and state != "shuffle":
                    state = "win"
                hole_x, hole_y = hole_next_x, hole_next_y
                # pygame.mixer.Sound.play(click_sound)
            # else:
            #    pygame.mixer.Sound.play(fart_sound)

        screen.fill((0, 170, 0))

        if state == "shuffle":
            shuffle_meter -= 1
            if shuffle_meter == 0:
                state = "game"
            else:
                for x in range(4):
                    for y in range(4):
                        v = field[y][x]
                        if v is not None:
                            screen.blit(numbers[v], (width // 2 + 100 * (x - 2), height // 2 + 100 * (y - 2)))
                screen.blit(img_shuffle, (width // 2 - img_shuffle.get_width() // 2, 10))
        elif state == "game":
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
