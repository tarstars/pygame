import pygame
from queue import Queue



def find_route(maze, start_pos, end_pos):
    width, height = len(maze[0]), len(maze)
    que = Queue()
    visited = set()
    que.put(start_pos)
    visited.add(start_pos)
    bt = {}
    while not que.empty():
        v_current = que.get()
        for dp, dq in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            np, nq = v_current[0] + dp, v_current[1] + dq
            if 0 <= np < height and 0 <= nq < width and maze[np][nq] == "." and (np, nq) not in visited:
                que.put((np, nq))
                visited.add((np, nq))
                bt[(np, nq)] = v_current
    path = []
    if end_pos not in bt:
        return path
    pos = end_pos
    path.append(end_pos)
    while pos != start_pos:
        pos = bt[pos]
        path.append(pos)
    return path


def shift(xy):
    x, y = xy
    return x + 25, y + 25


def try_move(hero_pos, maze, dp, dq):
    p, q = hero_pos
    width, height = len(maze[0]), len(maze)
    np, nq = p + dp, q + dq
    if 0 <= np < height and 0 <= nq < width and maze[np][nq] == ".":
        return np, nq
    return hero_pos


def screen_coords(p, q):
    return q * 50, 10 + p * 51


def find_person(maze, search):
    for p, row in enumerate(maze):
        for q, c in enumerate(row):
            if c == search:
                return p, q


def draw_ground(screen, width, height, img_torch, img_bricks, maze):
    for p, line in enumerate(maze):
        for q, c in enumerate(line):
            img = {"B": img_bricks, "F": img_torch}.get(c)
            if img is not None:
                screen.blit(img, screen_coords(p, q))



def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    maze = [list(l) for l in open("Scene").readlines()]
    hero_pos = find_person(maze, 'H')
    maze[hero_pos[0]][hero_pos[1]] = "."
    enemy_pos = find_person(maze, 'E')
    maze[enemy_pos[0]][enemy_pos[1]] = "."
    img_torch = pygame.image.load(r"Images\torch_50.jpg")
    img_bricks = pygame.image.load(r"Images\bricks_50.jpg")
    print(hero_pos)
    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero_pos = try_move(hero_pos, maze, -1, 0)
                elif event.key == pygame.K_a:
                    hero_pos = try_move(hero_pos, maze, 0, -1)
                elif event.key == pygame.K_s:
                    hero_pos = try_move(hero_pos, maze, 1, 0)
                elif event.key == pygame.K_d:
                    hero_pos = try_move(hero_pos, maze, 0, 1)
        screen.fill((0, 0, 0))
        draw_ground(screen, width, height, img_torch, img_bricks, maze)
        pygame.draw.circle(screen, (0, 250, 0), shift(screen_coords(hero_pos[0], hero_pos[1])), 25)
        pygame.draw.circle(screen, (250, 0, 0), shift(screen_coords(enemy_pos[0], enemy_pos[1])), 25)
        path = find_route(maze, enemy_pos, hero_pos)
        old_pos = None
        for pos in path:
            if old_pos is not None:
                pygame.draw.line(screen, (250, 250, 0), shift(screen_coords(old_pos[0], old_pos[1])), shift(screen_coords(pos[0], pos[1])))
            old_pos = pos
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
