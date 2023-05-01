import pygame
import math


def draw_scene(screen, width, height, t, selected_circle):
    pygame.draw.circle(
        screen,
        (0, 255, 0),
        (width // 2 + math.cos(2 / 5 * math.pi * selected_circle + t) * 300,
         height // 2 - math.sin(2 / 5 * math.pi * selected_circle + t) * 300), 15)

    for circle_index in range(5):
        pygame.draw.circle(
            screen,
            (250, 0, 0),
            (width // 2 + math.cos(2 / 5 * math.pi * circle_index + t) * 300,
             height // 2 - math.sin(2 / 5 * math.pi * circle_index + t) * 300), 10)



def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    t = 0

    selected_circle = 0

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected_circle += 1
                elif event.key == pygame.K_RIGHT:
                    selected_circle -= 1
        screen.fill((0, 170, 0))
        draw_scene(screen, width, height, t, selected_circle)

        t += 0.01
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
