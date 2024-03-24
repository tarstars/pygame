import pygame


def find_point(a, pos):
    for ind, arr_pos in enumerate(a):
        dp , dq = pos[0] - arr_pos[0], pos[1] - arr_pos[1]
        if dp ** 2 + dq ** 2 <= 100:
            return ind

def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    clock = pygame.time.Clock()
    clicked_points = []
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    clicked_points.append(pygame.mouse.get_pos())
                elif pygame.mouse.get_pressed()[2]:
                    ind = find_point(clicked_points, pygame.mouse.get_pos())
                    print(ind)
        screen.fill((0, 170, 0))
        for v in clicked_points:
            pygame.draw.circle(screen, (250, 250, 0), v, 10)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
