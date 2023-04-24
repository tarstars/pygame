import random




import pygame


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    clock = pygame.time.Clock()
    while running:
        clock.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 128, 255))
        pygame.draw.rect(surface=screen, color=(0, 0, 0), rect=(0, 0, 100, 70))
        for times in range(20, 1000, 10):
            pygame.draw.circle(surface=screen, color=(250, 250, 0), center=(times, 100), radius=100)
        for _ in range(30):
            pygame.draw.arc(surface=screen, color=(0, 255, 255), rect=(random.randint(10, width), random.randint(10, height), 70, 70), start_angle=0, stop_angle=3.14,
                            width=3)
        for _ in range(30):
            pygame.draw.arc(surface=screen, color=(255, 255, 255), rect=(random.randint(10, width), random.randint(10, height), 90, 80), start_angle=4.16, stop_angle=3.14,
                            width=8)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()