import pygame


def find_hero(maze):
    for p, row in enumerate(maze):
        for q, c in enumerate(row):
            if c == "H":
                return p, q


def draw_ground(screen, width, height, img_torch, img_bricks, maze):
    p = 0
    for line in maze:
        v = 0
        for c in line:
            if c == "B":
                screen.blit(img_bricks, (v, 10 + p * 51))
            elif c == "F":
                screen.blit(img_torch, (v, 10 + p * 51))
            v += 50
        p += 1



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
        screen.fill((0, 0, 0))
        draw_ground(screen, width, height, img_torch, img_bricks, maze)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
