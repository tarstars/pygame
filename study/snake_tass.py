import random

import pygame

PYTHON_R = 40

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


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    dx, dy = PYTHON_R, 0
    cx, cy = width // 2, height // 2
    x, y = cx, cy

    apple_x, apple_y = 0, 0
    apple = False

    q = OurQueue(1000)

    clock = pygame.time.Clock()
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx, dy = -PYTHON_R, 0
                elif event.key == pygame.K_w:
                    dx, dy = 0, -PYTHON_R
                elif event.key == pygame.K_s:
                    dx, dy = 0, PYTHON_R
                elif event.key == pygame.K_d:
                    dx, dy = PYTHON_R, 0

        if not apple:
            apple = True
            apple_x, apple_y = random.randint(1, width // PYTHON_R - 1) * PYTHON_R, random.randint(1, height // PYTHON_R - 1) * PYTHON_R  # TODD: repeat while apple is in snake

        x, y = x + dx, y + dy

        if (x, y) in set(q):
            print("snake eats itself")

        q.push((x, y))
        if len(q) > 20 and (x, y) != (apple_x, apple_y):
            q.pop()

        if (x, y) == (apple_x, apple_y):
            apple = False

        screen.fill((0, 70, 0))

        # set(q) - set of coordinates of snake's body
        # (apple_x, apple_y) in set(q) - check whether apple is inside the snake
                
        for pos in q:
            pygame.draw.circle(surface=screen, color=(125, 125, 0), center=pos, radius=PYTHON_R // 2)
        if apple:
            pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(apple_x, apple_y), radius=PYTHON_R // 2)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()


# python eats an apple: x == apple_x and y == apple_y
# we are to cut a tail === python doesn't eat an apple 
#        not (x == apple_x and y == apple_y)
#            (x != apple_x or y != apple_y)



