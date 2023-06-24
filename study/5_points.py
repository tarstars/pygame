import random

import pygame
import math


class OurQueue:
    def __init__(self, n):
        self.a = [0] * n
        self.n = len(self.a)
        self.r = 0
        self.l = 0

    def push(self, v):
        self.a[self.r] = v
        self.r = (self.r + 1) % self.n

    def peek(self):
        return self.a[self.l]

    def pop(self):
        self.l = (self.l + 1) % self.n

    def empty(self):
        return self.r == self.l

    def __iter__(self):
        def queue_iterator():
            current_pos = self.l
            while current_pos != self.r:
                yield self.a[current_pos]
                current_pos = (current_pos + 1) % self.n
        return queue_iterator()

    def __len__(self):
        if self.l <= self.r:
            return self.r - self.l
        return self.n - (self.l - self.r)


def draw_penta(screen, t, x, y, color, c):
    for r in range(c):
        pygame.draw.circle(surface=screen, color=color, center=circle_point(r, t, x, y, c), radius=10)
        for v in range(1, c):
            pygame.draw.line(surface=screen, color=color, start_pos=circle_point(r, t, x, y, c), end_pos=circle_point(r + v, t, x, y, c))


def circle_point(r, t, x, y, c):
    return (x + math.cos(2 / c * math.pi * r + t) * 70, y + math.sin(2 / c * math.pi * r + t) * 70)



def main():
    c = 5
    meter = 0
    q = OurQueue(22)
    a = []
    t = 0
    n = 3
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True


    clock = pygame.time.Clock()
    while running:
        meter += 1
        if meter == 10:
            meter = 0
            color = (random.randint(0, 255), random.randint(0, 255),  random.randint(0, 255))
            q.push((random.randint(0, width), random.randint(0, height), color))
        if len(q) > 20:
            q.pop()
        clock.tick(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((250, 250, 250))
        t += 0.01
        for x, y, color in q:
            draw_penta(screen, t, x, y, color, c)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
