import pygame
import math



def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    t=0

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))
        for r in range(5):
            pygame.draw.circle(screen, (250, 0, 0), (600 + math.cos(2/5*math.pi*r+t) * 300, 400 - math.sin(2/5*math.pi*r+t) * 300), 10)
        for r in range(5):
            pygame.draw.circle(screen, (250, 0, 0), (600 + math.cos(2/5*math.pi*r+t) * 300, 400 + math.sin(2/5*math.pi*r+t) * 300), 10)
        pygame.draw.line(surface=screen,
                         color=(0, 0, 255),
                         start_pos=(600 + math.cos(2/5*math.pi*r+t) * 300, 0),
                         end_pos=(600 + math.cos(2 / 5 * math.pi * r + t) * 300, height),
                         width=2
                         )

        t+=0.01
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
