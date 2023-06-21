import pygame
import math



def draw_penta(screen, t, x, y):
    for r in range(5):
        pygame.draw.circle(surface=screen, color=(250, 0, 0), center=circle_point(x + r, y + t), radius=10)
        pygame.draw.line(surface=screen, color=(250, 0, 0), start_pos=circle_point(x + r, y + t), end_pos=circle_point(x + r + 3, y + t))



def circle_point(r, t):
    return (600 + math.cos(2 / 5 * math.pi * r + t) * 300, 400 + math.sin(2 / 5 * math.pi * r + t) * 300)



def main():
    t = 0
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
        t += 0.01
        draw_penta(screen, t, 10, 200)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
