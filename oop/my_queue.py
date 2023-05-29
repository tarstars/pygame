import unittest


class OurQueue:
    def __init__(self):
        self.a = [0] * 1000000
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


class TestOurQueue(unittest.TestCase):
    def test_create(self):
        our_queue = OurQueue()
        self.assertTrue(our_queue.empty())
        our_queue.push(0)
        our_queue.push(1)
        self.assertEqual(0, our_queue.peek())
        self.assertFalse(our_queue.empty())
        our_queue.pop()
        self.assertEqual(1, our_queue.peek())