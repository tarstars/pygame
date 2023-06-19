import random

import pygame


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



PYTHON_R = 40


def main():
    fail_sound = pygame.mixer.Sound("../Sounds/fail.mp3")
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True
    dx = PYTHON_R
    dy = 0
    x = width // 2
    y = height // 2
    apple = False
    apple_x = 0
    apple_y = 0

    queue = OurQueue(1000)
    pew_sound = pygame.mixer.Sound("../Sounds/a8887ebd8bd4435.mp3")

    clock = pygame.time.Clock()
    while running:
        clock.tick(10)

        if not apple:
            apple_x = random.randint(0, width // PYTHON_R) * PYTHON_R
            apple_y = random.randint(0, height // PYTHON_R) * PYTHON_R
            apple = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx = -PYTHON_R
                    dy = 0
                elif event.key == pygame.K_w:
                    dx = 0
                    dy = -PYTHON_R
                elif event.key == pygame.K_s:
                    dx = 0
                    dy = PYTHON_R
                elif event.key == pygame.K_d:
                    dx = PYTHON_R
                    dy = 0
                elif event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(pew_sound)
        x, y = x + dx, y + dy
        if (x, y) in queue:
            running = False
        queue.push((x, y))
        if len(queue) > 20 and (x, y) != (apple_x, apple_y):
            queue.pop()
        if apple_x == x and apple_y == y:
            apple = False

        screen.fill((0, 170, 0))
        if (apple_x, apple_y) in queue:
            apple = False
        if x > width or y > height or x < 0 or y < 0:
            running = False
        for v in queue:
            pygame.draw.circle(screen, (50, 250, 50), v, PYTHON_R // 2)
        if apple:
            pygame.draw.circle(screen, (250, 0, 0), (apple_x, apple_y), PYTHON_R // 2)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
