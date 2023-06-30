from itertools import groupby

import pygame

DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
DIRECTION_NAMES = ["вправо", "вверх", "влево", "вниз"]


def trace_picture(picture, active_point):
    visited = set()
    pq = active_point
    direction_index = 0  # starting direction: right
    while True:
        visited.add((pq, direction_index))
        for i in [0, -1, 1, 2]:  # Try to turn right, go straight, turn left, or turn around
            next_index = (direction_index + i) % 4
            dp, dq = DIRECTIONS[next_index]
            next_pq = pq[0] + dp, pq[1] + dq
            if next_pq in picture:
                yield DIRECTION_NAMES[next_index]
                pq = next_pq
                direction_index = next_index
                break
        else:
            break
        if pq == active_point and len(visited) > 1:
            break


def number_to_russian(n):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]

    if 1 <= n < 10:
        return ones[n]
    elif 10 < n < 20:
        return teens[n-10]
    elif 10 <= n < 100:
        return tens[n//10] + (' ' + ones[n%10] if (n%10 != 0) else '')
    else:
        return 'сто'


def compress_directions(directions):
    for direction, group in groupby(directions):
        count = len(list(group))
        yield f"{number_to_russian(count)} {direction}"


def dump_picture(picture, active_point):
    full_picture = []
    for compressed_direction in compress_directions(trace_picture(picture, active_point)):
        full_picture.append(compressed_direction)
    with open('our_picture.txt', 'w') as dst:
        dst.write('\n'.join(full_picture))


def draw_grid(screen, width, height, grid_step):
    for x in range(0, width, grid_step):
        pygame.draw.line(surface=screen, color=(75, 75, 75), start_pos=(x, 0), end_pos=(x, height))

    for y in range(0, height, grid_step):
        pygame.draw.line(surface=screen, color=(75, 75, 75), start_pos=(0, y), end_pos=(width, y))


def xy2sqpos(x, y, grid_step):
    q = x // grid_step
    p = y // grid_step
    return p, q


def sqpos2xy(pq, grid_step):
    p, q = pq
    x1 = q * grid_step
    y1 = p * grid_step
    x2 = x1 + grid_step
    y2 = y1 + grid_step
    return (x1, y1), (x2, y2)


def draw_selected(screen, grid_step, picture):
    for p, q in picture:
        (x1, y1), (x2, y2) = sqpos2xy((p, q), grid_step)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x1, y1, x2-x1, y2-y1))


def is_neighbor_of_existing_cell(pq, picture):
    p, q = pq
    for dp, dq in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # check right, down, left, up
        if (p + dp, q + dq) in picture:
            return True
    return False


def find_clusters(cells):
    def dfs(cell, visited, cluster):
        visited.add(cell)
        cluster.add(cell)
        p, q = cell
        for dp, dq in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # check right, down, left, up
            neighbor = (p + dp, q + dq)
            if neighbor in cells and neighbor not in visited:
                dfs(neighbor, visited, cluster)

    visited = set()
    clusters = []
    for cell in cells:
        if cell not in visited:
            cluster = set()
            dfs(cell, visited, cluster)
            clusters.append(cluster)
    return clusters


def draw_active_point(screen, grid_step, active_point):
    if active_point:
        (x1, y1), (x2, y2) = sqpos2xy(active_point, grid_step)
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x1, y1, x2-x1, y2-y1))


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    grid_step = 25
    picture = set()
    active_point = None

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and active_point is not None:
                    dump_picture(picture, active_point)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                pq = xy2sqpos(x, y, grid_step)
                if event.button == 1:  # 1 indicates the left mouse button
                    lt, rb = sqpos2xy(pq, grid_step)
                    if pq in picture:
                        picture.remove(pq)
                        if len(find_clusters(picture)) > 1:
                            picture.add(pq)  # deletion resulted in multiple clusters, undo it
                    else:
                        if not picture or is_neighbor_of_existing_cell(pq, picture):
                            picture.add(pq)
                elif event.button == 3:
                    if pq in picture:
                        active_point = pq

        screen.fill((0, 0, 0))

        draw_grid(screen, width, height, grid_step)
        draw_selected(screen, grid_step, picture)
        draw_active_point(screen, grid_step, active_point)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
