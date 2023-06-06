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


def main():
    shape = width, height = (1200, 800)
    pygame.init()
    screen = pygame.display.set_mode(shape)
    running = True

    dx, dy = 10, 0
    cx, cy = width // 2, height // 2
    x, y = cx, cy
    q = OurQueue(1000)

    clock = pygame.time.Clock()
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    dx, dy = -10, 0
                elif event.key == pygame.K_w:
                    dx, dy = 0, -10
                elif event.key == pygame.K_s:
                    dx, dy = 0, 10
                elif event.key == pygame.K_d:
                    dx, dy = 10, 0

        x, y = x + dx, y + dy
        q.push((x, y))
        if len(q) > 20:
            q.pop()

        screen.fill((0, 170, 0))

        for pos in q:
            pygame.draw.circle(surface=screen, color=(255, 0, 0), center=pos, radius=10)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
