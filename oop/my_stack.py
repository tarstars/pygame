import unittest


class OurStack_00:
    def __init__(self):
        self.data = []

    def push(self, v):
        self.data.append(v)

    def peek(self):
        return self.data[-1]

    def pop(self):
        return self.data.pop()


class OurStack:
    def __init__(self):
        self.a = [0] * 1000
        self.n = 0

    def push(self, v):
        self.a[self.n] = v
        self.n += 1

    def pop(self):
        self.n -= 1
        return self.a[self.n]

    def peek(self):
        return self.a[self.n - 1]


class TestOurStack(unittest.TestCase):
    def test_create(self):
        our_stack = OurStack()
        our_stack.push(13)
        self.assertEqual(13, our_stack.peek())
        our_stack.push(4)
        self.assertEqual(4, our_stack.peek())
        self.assertEqual(4, our_stack.pop())
        self.assertEqual(13, our_stack.peek())
