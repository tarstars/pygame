import random
from typing import List, Optional

import copy
import pygame


def find_hole(field: List[List[Optional[int]]]):
    """Finds the position of a hole on board.

    :param field: a field for 15 game
    :return: a tuple with x, y coordinates of a hole
    """
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] is None:
                return x, y


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    numbers = [pygame.image.load(f"../Numbers/{v}.jpg") for v in range(1, 16)]
    click_sound = pygame.mixer.Sound("../Sounds/click.mp3")
    fail_sound = pygame.mixer.Sound("../Sounds/fail.mp3")
    win_music = pygame.mixer.Sound("../Sounds/win.mp3")
    reload_sound = pygame.mixer.Sound("../Sounds/reload.mp3")
    field_solved = [[0, 1, 2, 3],
                    [4, 5, 6, 7],
                    [8, 9, 10, 11],
                    [12, 13, 14, None]]
    field = [[10, 13, 12, 3],
            [4, 5, 7, 6],
            [8, 9, 0, 11],
            [2, 14, 1, None]]
    field_copy = [[10, 13, 12, 3],
                [4, 5, 7, 6],
                [8, 9, 0, 11],
                [2, 14, 1, None]]
    state = "shuffle"
    shuffle_meter = 300
    hole_x, hole_y = find_hole(field)

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        hole_next_x, hole_next_y = hole_x, hole_y
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif state == "shuffle" or event.type == pygame.KEYDOWN:
                if state == "game":
                    my_key = event.key
                elif state == "shuffle":
                    my_key = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP][random.randint(0, 3)]
                if my_key == pygame.K_LEFT:
                    hole_next_x -= 1
                elif my_key == pygame.K_RIGHT:
                    hole_next_x += 1
                elif my_key == pygame.K_UP:
                    hole_next_y -= 1
                elif my_key == pygame.K_DOWN:
                    hole_next_y += 1
                elif my_key == pygame.K_a:
                    hole_next_x -= 1
                elif my_key == pygame.K_d:
                    hole_next_x += 1
                elif my_key == pygame.K_w:
                    hole_next_y -= 1
                elif my_key == pygame.K_s:
                    hole_next_y += 1
                elif my_key == pygame.K_SPACE:
                    field = copy.deepcopy(field_copy)
                    hole_x, hole_y = find_hole(field)
                    hole_next_x, hole_next_y = hole_x, hole_y
                    pygame.mixer.Sound.play(reload_sound)

        if (hole_x, hole_y) != (hole_next_x, hole_next_y):
            if 0 <= hole_next_x < 4 and 0 <= hole_next_y < 4:
                field[hole_y][hole_x], field[hole_next_y][hole_next_x] = field[hole_next_y][hole_next_x], field[hole_y][hole_x]
                if field == field_solved:
                    state = "play_win_sound"
                hole_x, hole_y = hole_next_x, hole_next_y
                pygame.mixer.Sound.play(click_sound)
            else:
                pygame.mixer.Sound.play(fail_sound)
        screen.fill((0, 170, 0))
        if state == "shuffle":
            shuffle_meter -= 1
            if shuffle_meter == 0:
                state = "game"
        elif state == "game":
            for x in range(4):
                for y in range(4):
                    v = field[y][x]
                    if v is not None:
                        screen.blit(numbers[v], (width // 2 + 100 * (x - 2), height // 2 + 100 * (y - 2)))
        elif state == "play_win_sound":
            pygame.mixer.Sound.play(win_music)
            state = "win"
        elif state == "win":
            pass

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
