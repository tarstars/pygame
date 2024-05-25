import random

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


def draw_path(screen, path):
    old_pos = None
    for pos in path:
        if old_pos is not None:
            pygame.draw.line(screen, (250, 250, 0), shift(screen_coords(old_pos[0], old_pos[1])),
                             shift(screen_coords(pos[0], pos[1])))
        old_pos = pos


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
    return q * 50, 10 + (p + 1) * 50


def find_person(maze, search):
    for p, row in enumerate(maze):
        for q, c in enumerate(row):
            if c == search:
                return p, q


def draw_ground(screen, img_bricks, maze):
    for pos in maze.get_walls():
        screen.blit(img_bricks, screen_coords(*pos))


class Hero:
    def __init__(self):
        self.sanity = 10
        self.hero_costumes = [pygame.image.load(f"Images/Hero_{v}.png") for v in (1, 2, 3)]
        self.pos = None

    def damage(self):
        self.sanity -= 1

    def draw(self, screen, hero_angle):
        rotated_hero = pygame.transform.rotate(self.get_costume(), hero_angle)
        screen.blit(rotated_hero, screen_coords(self.pos[0], self.pos[1]))

    def dead(self):
        return self.sanity == 0

    def get_costume(self):
        if self.sanity > 7:
            return self.hero_costumes[0]
        if self.sanity > 5:
            return self.hero_costumes[1]
        return self.hero_costumes[2]


class ButterFly:
    def __init__(self, pos):
        self.image = pygame.image.load(r"Images/Butter_1.png")
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, screen_coords(*self.pos))

    def next(self):
        p, q = self.pos
        dp, dq = [(-1, 0), (0, -1), (1, 0), (0, 1)][random.randint(0, 3)]
        np, nq = p + dp, q + dq
        self.pos = np, nq

    def in_maze(self, height, width):
        p, q = self.pos
        return (0 <= p < height) and (0 <= q < width)


class Ant:
    def __init__(self, pos):
        self.pos = pos
        self.cp = 25
        self.sugar_amount = 0
        self.angle = 0
        self.images = [pygame.image.load(f"Images//C_Ant_{num}.png") for num in range(1, 6)]

    def set_pos(self, new_pos):
        p, q = self.pos
        np, nq = new_pos
        dp, dq = np - p, nq - q
        self.angle = {(-1, 0): 0, (0, -1): 90, (1, 0): 180, (0, 1): 270}[(dp, dq)]
        self.pos = new_pos

    def draw(self, screen):
        rotated_ant = pygame.transform.rotate(self.images[(self.cp - 1) // 5], self.angle)
        screen.blit(rotated_ant, screen_coords(self.pos[0], self.pos[1]))


class Sugar:
    def __init__(self, pos):
        self.amount = 5
        self.pos = pos


class Brick:
    pass


class Coin:
    def __init__(self, pos):
        self.pos = pos
        self.image = pygame.image.load(r"Images/Coin.png")
        self.blinks = [pygame.image.load(f"Images/Blink_{v}.png") for v in (1, 2, 3)]
        self.active = True

    def draw(self, screen, time):
        if self.active:
            screen.blit(self.image, screen_coords(*self.pos))
            if not random.randint(0, 4):
                screen.blit(self.blinks[random.randint(0, 2)], screen_coords(*self.pos))


class Maze:
    def __init__(self, data):
        self.data = data
        self.height, self.width = len(data), len(data[0])
        self.brick_coords = set()
        self.coins = []
        self.sugars = []
        self.pos2obj = {}
        self.butterflies = []
        for p, line in enumerate(data):
            for q, c in enumerate(line):
                pos = p, q
                if c == "B":
                    self.brick_coords.add(pos)
                    self.pos2obj[pos] = Brick()
                if c == "C":
                    coin = Coin(pos)
                    self.coins.append(coin)
                    self.pos2obj[pos] = coin
                if c == "S":
                    sugar = Sugar(pos)
                    self.sugars.append(sugar)
                    self.pos2obj[pos] = sugar

    def is_available(self, pos):
        return (pos not in self.brick_coords) and (pos not in self.brick_coords)

    def get_walls(self):
        return self.brick_coords

    def draw(self, screen, time):
        for butterfly in self.butterflies:
            butterfly.draw(screen)
        for coin in self.coins:
            coin.draw(screen, time)

    def next(self):
        for butterfly in self.butterflies:
            butterfly.next()

    def clean_up(self):
        self.butterflies = [b for b in self.butterflies if b.in_maze(self.height, self.width)]


def load_level(file_name):
    data = [list(line) for line in open(file_name).readlines()]

    hero_pos = find_person(data, 'H')
    enemy_pos = find_person(data, 'E')

    maze = Maze(data)

    return maze, hero_pos, enemy_pos


def main():
    shape = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    time = 0
    coins = 0
    hero = Hero()

    maze, hero.pos, enemy_pos = load_level("Level_1")
    ant = Ant(enemy_pos)
    del enemy_pos

    img_walls = pygame.image.load(r"Images/Dirt_1.png")
    img_sugar = pygame.image.load(r"Images/Sugar_1.png")

    font = pygame.font.SysFont(None, 100)
    img_coins = font.render(f"{coins}", True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    hero_angle = 0

    clock = pygame.time.Clock()
    while running:
        clock.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.pos = try_move(hero.pos, maze, -1, 0)
                    hero_angle = 0
                elif event.key == pygame.K_a:
                    hero.pos = try_move(hero.pos, maze, 0, -1)
                    hero_angle = 90
                elif event.key == pygame.K_s:
                    hero.pos = try_move(hero.pos, maze, 1, 0)
                    hero_angle = 180
                elif event.key == pygame.K_d:
                    hero.pos = try_move(hero.pos, maze, 0, 1)
                    hero_angle = 270
        screen.fill((108, 60, 12))

        draw_ground(screen, img_walls, maze)

        hero.draw(screen, hero_angle)

        screen.blit(img_coins, (shape[0] - img_coins.get_width(), 0))

        for sugar_piece in maze.sugars:
            if sugar_piece.amount:
                screen.blit(img_sugar, screen_coords(sugar_piece.pos[0], sugar_piece.pos[1]))

        if ant is not None:
            ant.draw(screen)

            if ant.pos in maze.pos2obj and isinstance(maze.pos2obj[ant.pos], Sugar):
                ant.sugar_amount += maze.pos2obj[ant.pos].amount
                maze.pos2obj[ant.pos].amount = 0

            if ant.sugar_amount == 0:
                path = find_route(maze, ant.pos, hero.pos)
                if path:
                    ant.set_pos(path[-2])
                if ant.pos == hero.pos:
                    hero.damage()
            else:
                ant.sugar_amount -= 1
                ant.cp = max(0, ant.cp - 1)
                if ant.cp == 0:
                    maze.butterflies.append(ButterFly(ant.pos))
                    ant = None
        if hero.pos in maze.pos2obj and isinstance(maze.pos2obj[hero.pos], Coin):
            if maze.pos2obj[hero.pos].active:
                coins += 1
                img_coins = font.render(f"{coins}", True,
                                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            maze.pos2obj[hero.pos].active = False

        maze.draw(screen, time)
        maze.next()
        maze.clean_up()
        running = running and (ant is not None or maze.butterflies)

        time += 1

        if hero.dead():
            running = False

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
