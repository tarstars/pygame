import pygame


def transform(img):
    return pygame.transform.scale(img, (50, 100))


def main():
    shape = width, height = (1200, 1300)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    pencil_colors = ["green", "magenta", "yellow"]
    selected = "_selected"

    image_pencils = [transform(pygame.image.load("../Pencils/" + color + ".jpg")) for color in pencil_colors]
    image_pencils_selected = [transform(pygame.image.load("../Pencils/" + color + selected + ".jpg")) for color in
                              pencil_colors]

    clock = pygame.time.Clock()
    while running:
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))

        cx, cy = width // 2, height // 2
        for pos, normal_pencil in enumerate(image_pencils):
            screen.blit(normal_pencil, (10 + pos * 350, cy - 100))
        for pos, selected_pencil in enumerate(image_pencils_selected):
            screen.blit(selected_pencil, (10 + pos * 350, cy))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
