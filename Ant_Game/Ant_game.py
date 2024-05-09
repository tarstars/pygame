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
    for pos in maze.get_walls():
        screen.blit(img_bricks, screen_coords(*pos))
    for pos in maze.get_torches():
        screen.blit(img_torch, screen_coords(*pos))


class Ant:
    def __init__(self, pos):
        self.pos = pos
        self.cp = 25
        self.sugar_amount = 0
        self.angle = 0
        self.img_5 = pygame.image.load(r"Images/C_Ant_5.png")

    def set_pos(self, new_pos):
        p, q = self.pos
        np, nq = new_pos
        dp, dq = np - p, nq - q
        self.angle = {(-1, 0): 0, (0, -1): 90, (1, 0): 180, (0, 1): 270}[(dp, dq)]
        self.pos = new_pos

    def draw(self, screen):
        rotated_ant = pygame.transform.rotate(self.img_5, self.angle)
        screen.blit(rotated_ant, screen_coords(self.pos[0], self.pos[1]))


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

    def get_walls(self):
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
    img_walls = pygame.image.load(r"Images/Dirt_1.png")
    img_hero_1 = pygame.image.load(r"Images/Hero_1.png")
    img_sugar = pygame.image.load(r"Images/Sugar_1.png")
    hero_angle = 0

    clock = pygame.time.Clock()
    while running:
        clock.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero_pos = try_move(hero_pos, maze, -1, 0)
                    hero_angle = 0
                elif event.key == pygame.K_a:
                    hero_pos = try_move(hero_pos, maze, 0, -1)
                    hero_angle = 90
                elif event.key == pygame.K_s:
                    hero_pos = try_move(hero_pos, maze, 1, 0)
                    hero_angle = 180
                elif event.key == pygame.K_d:
                    hero_pos = try_move(hero_pos, maze, 0, 1)
                    hero_angle = 270
        screen.fill((108, 60, 12))

        draw_ground(screen, img_torch, img_walls, maze)

        rotated_hero = pygame.transform.rotate(img_hero_1, hero_angle)
        screen.blit(rotated_hero, screen_coords(hero_pos[0], hero_pos[1]))

        ant.draw(screen)

        for sugar_piece in maze.sugars:
            # pygame.draw.circle(screen, (255, 255, 255), shift(screen_coords(sugar_piece.pos[0], sugar_piece.pos[1])), 25)
            screen.blit(img_sugar, screen_coords(sugar_piece.pos[0], sugar_piece.pos[1]))

        if ant.pos in maze.pos2obj and isinstance(maze.pos2obj[ant.pos], Sugar):
            ant.sugar_amount += maze.pos2obj[ant.pos].amount
            maze.pos2obj[ant.pos].amount = 0

        if ant.sugar_amount == 0:
            path = find_route(maze, ant.pos, hero_pos)
            if path:
                ant.set_pos(path[-2])
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
