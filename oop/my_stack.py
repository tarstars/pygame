import unittest


class OurStack:
    def __init__(self):
        self.data = []

    def push(self, v):
        self.data.append(v)

    def peek(self):
        return self.data[-1]

    def pop(self):
        return self.data.pop()


class TestOurStack(unittest.TestCase):
    def test_create(self):
        our_stack = OurStack()
        our_stack.push(13)
        self.assertEqual(our_stack.peek(), 13)
        our_stack.push(4)
        self.assertEqual(our_stack.peek(), 4)
        our_stack.pop()
        self.assertEqual(our_stack.peek(), 13)
