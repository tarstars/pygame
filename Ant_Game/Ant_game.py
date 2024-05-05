import pygame
from queue import Queue



def find_route(maze, start_pos, end_pos):
    width, height = maze.width, maze.height
    que = Queue()
    visited = set()
    que.put(start_pos)
    visited.add(start_pos)
    bt = {}
    while not que.empty():
        v_current = que.get()
        for dp, dq in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            np, nq = v_current[0] + dp, v_current[1] + dq
            if 0 <= np < height and 0 <= nq < width and maze.is_available((np, nq)) and (np, nq) not in visited:
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
    width, height = maze.width, maze.height
    np, nq = p + dp, q + dq
    if 0 <= np < height and 0 <= nq < width and maze.is_available((np, nq)):
        return np, nq
    return hero_pos


def screen_coords(p, q):
    return q * 50, 10 + p * 50


def find_person(maze, search):
    for p, row in enumerate(maze):
        for q, c in enumerate(row):
            if c == search:
                return p, q


def draw_ground(screen, img_torch, img_bricks, maze):
    for pos in maze.get_bricks():
        screen.blit(img_bricks, screen_coords(*pos))
    for pos in maze.get_torches():
        screen.blit(img_torch, screen_coords(*pos))


class Ant:
    def __init__(self, pos):
        self.pos = pos
        self.cp = 25
        self.sugar_amount = 0


class Sugar:
    def __init__(self, pos):
        self.amount = 5
        self.pos = pos


class Brick:
    pass


class Torch:
    pass


class Maze:
    def __init__(self, data):
        self.data = data
        self.height, self.width = len(data), len(data[0])
        self.brick_coords = set()
        self.torch_coords = set()
        self.sugars = []
        self.pos2obj = {}
        for p, line in enumerate(data):
            for q, c in enumerate(line):
                if c == "B":
                    self.brick_coords.add((p, q))
                    self.pos2obj[(p, q)] = Brick()
                if c == "T":
                    self.torch_coords.add((p, q))
                    self.pos2obj[(p, q)] = Torch()
                if c == "S":
                    sugar = Sugar((p, q))
                    self.sugars.append(sugar)
                    self.pos2obj[(p, q)] = sugar

    def is_available(self, pos):
        return (pos not in self.brick_coords) and (pos not in self.brick_coords)

    def get_bricks(self):
        return self.brick_coords

    def get_torches(self):
        return self.torch_coords


def load_level(file_name):
    data = [list(line) for line in open(file_name).readlines()]

    hero_pos = find_person(data, 'H')
    enemy_pos = find_person(data, 'E')

    maze = Maze(data)

    return maze, hero_pos, enemy_pos


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    maze, hero_pos, enemy_pos = load_level("Level_1")
    ant = Ant(enemy_pos)
    del enemy_pos

    img_torch = pygame.image.load(r"../study/Images/torch_50.jpg")
    img_bricks = pygame.image.load(r"../study/Images/bricks_50.jpg")

    clock = pygame.time.Clock()
    while running:
        clock.tick(3)
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

        draw_ground(screen, img_torch, img_bricks, maze)

        pygame.draw.circle(screen, (0, 250, 0), shift(screen_coords(hero_pos[0], hero_pos[1])), 25)

        pygame.draw.circle(screen, (250, 0, 0), shift(screen_coords(ant.pos[0], ant.pos[1])), 25)

        for sugar_piece in maze.sugars:
            pygame.draw.circle(screen, (255, 255, 255), shift(screen_coords(sugar_piece.pos[0], sugar_piece.pos[1])), 25)

        if ant.pos in maze.pos2obj and isinstance(maze.pos2obj[ant.pos], Sugar):
            ant.sugar_amount += maze.pos2obj[ant.pos].amount
            maze.pos2obj[ant.pos].amount = 0

        if ant.sugar_amount == 0:
            path = find_route(maze, ant.pos, hero_pos)
            if path:
                ant.pos = path[-2]
            if ant.pos == hero_pos:
                running = False
        else:
            ant.sugar_amount -= 1
            ant.cp = max(0, ant.cp - 1)

        old_pos = None
        for pos in path:
            if old_pos is not None:
                pygame.draw.line(screen, (250, 250, 0), shift(screen_coords(old_pos[0], old_pos[1])), shift(screen_coords(pos[0], pos[1])))
            old_pos = pos
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
