import pygame
from queue import Queue


def find_point(a, pos):
    for ind, arr_pos in enumerate(a):
        dp , dq = pos[0] - arr_pos[0], pos[1] - arr_pos[1]
        if dp ** 2 + dq ** 2 <= 100:
            return ind


def skip_ind(v, p):
    return v if v < p else v - 1


def recalc_graph(g, p):
    return {skip_ind(k, p): {skip_ind(vv, p) for vv in v if vv != p} for k,v in g.items() if k != p}



def shortest(start_pos, end_pos, g):
    q = Queue()
    visited = set()
    bt = {}
    q.put(start_pos)
    visited.add(start_pos)
    while not q.empty():
        v_current = q.get()
        for v in g.get(v_current, []):
            if v not in visited:
                visited.add(v)
                q.put(v)
                bt[v] = v_current
    if end_pos not in bt:
        return []
    pos = end_pos
    path = []
    while pos != start_pos:
        path.append(pos)
        pos = bt[pos]
    path.append(pos)
    return list(reversed(path))


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
    path = []
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    current_pos = pygame.mouse.get_pos()
                    current_ind = find_point(clicked_points, current_pos)
                    if current_ind is None:
                        clicked_points.append(pygame.mouse.get_pos())
                    else:
                        clicked_points.pop(current_ind)
                        start_pos = None
                        end_pos = None
                        sel_point = None
                        g = recalc_graph(g, current_ind)
                        path = []
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
                                path = shortest(start_pos, end_pos, g)
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
        prev = None
        for current in path:
            if prev is not None:
                pygame.draw.line(screen, (250, 0, 0), clicked_points[prev], clicked_points[current], 5)
            prev = current
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()