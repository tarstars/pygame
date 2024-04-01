import pygame
import random


def insertion_sort(a):
    n = len(a)
    for p in range(1, n):
        q = p
        while q > 0 and a[q] < a[q - 1]:
            a[q], a[q - 1] = a[q - 1], a[q]
            q -= 1
    return a


def partitioning(a, x):
    n = len(a)
    l = 0
    r = n - 1
    while l < r:
        while l < r and a[l] < x:
            l += 1
        while l < r and a[r] > x:
            r -= 1
        a[r], a[l] = a[l], a[r]
        pygame.display.update()
    return l, a


def min_sort(a):
    n = len(a)
    for p in range(n):
        min_q = p
        for q in range(p, n):
            if a[q] < a[min_q]:
                min_q = q
        a[p], a[min_q] = a[min_q], a[p]
    return a


def bub_sort(a):
    n = len(a)
    for v in range(n - 1, 0, -1):
        for p in range(v):
            if a[p] > a[p + 1]:
                a[p], a[p + 1] = a[p + 1], a[p]
                pygame.display.update()
    return a


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    a = list(range(20))
    random.shuffle(a)
    n = len(a)
    p = 0
    clock = pygame.time.Clock()
    while running:
        clock.tick(n / 20)

        if p < n - 1:
            min_q = p
            for q in range(p, n):
                if a[q] < a[min_q]:
                    min_q = q
            a[p], a[min_q] = a[min_q], a[p]
            p += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 170, 0))
        for q in range(n):
            x1 = width // n * q
            x2 = width // n * (q + 1)
            h = (a[q] * height) // n
            pygame.draw.rect(
                surface=screen,
                color=(0, 130, 9),
                rect=(x1, height - h, width // n, h)
            )
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
