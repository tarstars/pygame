import random

import pygame


def optimal_move(n):
    coll = n % 4
    if coll == 0:
        return random.randint(1, 3)
    else:
        return coll


def transform(img):
    return pygame.transform.scale(img, (50, 100))


def main():
    shape = width, height = (800, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    n = random.randint(5, 16)
    loose_background = pygame.image.load("../Backgrounds/Loose_background.PNG")
    background = pygame.image.load("../Backgrounds/background.PNG")
    p_unsel = transform(pygame.image.load("../Pencils/green.jpg"))
    p_sel = transform(pygame.image.load("../Pencils/green_selected.jpg"))
    state = "choosing"
    n_sel = 1
    font = pygame.font.SysFont(None, 100)
    img_win = font.render("YOU WIN!", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    game_over_sound = pygame.mixer.Sound("../Sounds/game_over.mp3")


    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if n_sel < min(n, 3):
                        n_sel += 1
                elif event.key == pygame.K_a:
                    if n_sel < min(n, 3):
                        n_sel += 1
                elif event.key == pygame.K_RIGHT:
                    if n_sel > 1:
                        n_sel -= 1
                elif event.key == pygame.K_d:
                    if n_sel > 1:
                        n_sel -= 1
                elif event.key == pygame.K_SPACE and state == "choosing":
                    n -= n_sel
                    if n == 0:
                        state = "win"
                        meter_win = 120
                    else:
                        state = "bot_choosing"
                        bot_meter = 120
                        bot_move = optimal_move(n)
                        message_text = f"I want to take {bot_move}"
                    img_text = font.render(message_text, True, (255, 0, 0))
        screen.fill((0, 170, 0))
        if state == "choosing":
            screen.blit(background, (0, 0))
            for v in range(n):
                screen.blit(p_unsel if v < n - n_sel else p_sel, (0 + v * p_unsel.get_width(), height // 2 + 100))
        elif state == "bot_choosing":
            screen.blit(img_text, (width // 2 - img_text.get_width() // 2, height // 2 - img_text.get_height() // 2))
            bot_meter -= 1
            if bot_meter == 0:
                state = "choosing"
                n -= bot_move
                n_sel = 1
                if n == 0:
                    state = "loose"
                    meter_loose = 120
        elif state == "win":
            screen.blit(img_win, (width // 2 - img_text.get_width() // 2, height // 2 - img_text.get_height() // 2))
            meter_win -= 1
            if meter_win == 0:
                running = False
        elif state == "loose":
            screen.blit(loose_background, (0, 0))
            pygame.mixer.Sound.play(game_over_sound)
            meter_loose -= 1
            if meter_loose == 0:
                running = False
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
