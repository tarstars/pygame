import unittest


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


class TestOurQueue(unittest.TestCase):
    def test_create(self):
        our_queue = OurQueue(1000)
        self.assertTrue(our_queue.empty())
        our_queue.push(0)
        our_queue.push(1)
        self.assertEqual(0, our_queue.peek())
        self.assertFalse(our_queue.empty())
        our_queue.pop()
        self.assertEqual(1, our_queue.peek())

    def test_iterate(self):
        our_queue = OurQueue(5)
        our_queue.push(1)
        our_queue.push(2)
        our_queue.push(3)

        self.assertEqual([1, 2, 3], list(our_queue))
        self.assertEqual(3, len(our_queue))

        our_queue.pop()
        our_queue.push(4)

        our_queue.pop()
        our_queue.push(5)

        our_queue.pop()
        our_queue.push(6)

        self.assertEqual([4, 5, 6], list(our_queue))
        self.assertEqual(3, len(our_queue))
