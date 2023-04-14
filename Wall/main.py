import pygame

def draw_ground(screen,width,height,img_torch,img_bricks):
    p = 0
    for line in open("Scene"):
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

    img_torch = pygame.image.load(r"Images\torch_50.jpg")
    img_bricks = pygame.image.load(r"Images\bricks_50.jpg")
    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        draw_ground(screen,width,height,img_torch,img_bricks)
        pygame.display.update()
    pygame.quit()

print("somebody want told me that world is gonna rowming i have do it only in shit")


if __name__ == "__main__":
    main()
