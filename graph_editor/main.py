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
    sel_point = None
    g = {}
    sel_start = False
    start_pos = None
    sel_end = False
    end_pos = None
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
                    if ind is not None:
                        if sel_start:
                            start_pos = ind
                            sel_start = False
                        elif sel_end:
                            end_pos = ind
                            sel_end = False
                            if start_pos is not None:
                                print(f"Ready to find path from {start_pos} to {end_pos}")
                        elif sel_point is None:
                            sel_point = ind
                        else:
                            if ind not in g:
                                g[ind] = set()
                            if sel_point not in g:
                                g[sel_point] = set()
                            g[ind].add(sel_point)
                            g[sel_point].add(ind)
                            sel_point = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    sel_start = True
                elif event.key == pygame.K_s:
                    sel_end = True
        screen.fill((0, 170, 0))
        if sel_point is not None:
            pygame.draw.circle(screen, (250, 0, 0), clicked_points[sel_point], 15)
        if start_pos is not None:
            pygame.draw.circle(screen, (0, 0, 250), clicked_points[start_pos], 15)
        if end_pos is not None:
            pygame.draw.circle(screen, (0, 250, 0), clicked_points[end_pos], 15)
        for v in clicked_points:
            pygame.draw.circle(screen, (250, 250, 0), v, 10)
        for source, destinations in g.items():
            for dest in destinations:
                pygame.draw.line(screen, (0, 0, 250), clicked_points[source], clicked_points[dest])
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()