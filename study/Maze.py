import pygame


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


def find_hero(maze):
    for p, row in enumerate(maze):
        for q, c in enumerate(row):
            if c == "H":
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
    maze = open("Scene").readlines()
    hero_pos = find_hero(maze)
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
        pygame.draw.circle(screen, (250, 0, 0), shift(screen_coords(hero_pos[0], hero_pos[1])), 25)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
