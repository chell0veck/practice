import unittest
from random import randint

from random import randint

class AnagramTest(unittest.TestCase):

    def test(self, sol):
        self.assertEqual(sol('go go go', 'gggooo'), True)
        self.assertEqual(sol('abc', 'cba'), True)
        self.assertEqual(sol('hi man', 'hi      man'), True)
        self.assertEqual(sol('aabbcc', 'aabbc'), False)
        self.assertEqual(sol('123', '1 2'), False)
        return 'ALL TEST CASES PASSED'


class TestPair(unittest.TestCase):

    def test(self, sol):
        self.assertEqual(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        self.assertEqual(sol([1, 2, 3, 1], 3), 1)
        self.assertEqual(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


class TestFinder(unittest.TestCase):

    def test(self, sol):
        self.assertEqual(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        self.assertEqual(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        self.assertEqual(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]), 6)
        print('ALL TEST CASES PASSED')


class LargeContTest(unittest.TestCase):

    def test(self, sol):
        self.assertEqual(sol([1, 2, -1, 3, 4, -1]), 9)
        self.assertEqual(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        self.assertEqual(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


class TestBalanceCheck(unittest.TestCase):

    def test(self, func):
        self.assertEqual(func('[](){[[[]]]}('), False)
        self.assertEqual(func('[{{{(())}}}]((()))'), True)
        self.assertEqual(func('[[[]])]'), False)
        return 'ALL TEST CASES PASSED'


class TestDec2Bin(unittest.TestCase):

    def test(self, func):
        case_number = 200
        array = []

        for i in range(case_number):
            val = randint(-2*32, 2*32)
            array.append(val)
            self.assertEqual(func(val), bin(val))

        return 'ALL TEST CASES PASSED'


class TestPalindrome(unittest.TestCase):

    def test(self, func):
        self.assertEqual(func('lsdkjfskf'), False)
        self.assertEqual(func('radar'), True)
        return 'ALL TEST CASES PASSED'


class TestRLE(unittest.TestCase):

    def test(self, func):
        self.assertEqual(func(''), '')
        self.assertEqual(func('AABBCC'), 'A2B2C2')
        self.assertEqual(func('AAABCCDDDDD'), 'A3B1C2D5')
        self.assertIn(func('AAABCCcDDDDD'), ['A3B1C2cD5', 'A3B1C2c1D5'])
        return 'ALL TEST CASES PASSED'


class SNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class TestCycleCheck(unittest.TestCase):

    def test(self, func):

        # Create cycle list:
        a, b, c = SNode(1), SNode(2), SNode(3)
        a.next = b; b.next = c; c.next = a

        # Create non cycle list:
        x, y, z = SNode(1), SNode(2), SNode(3)
        x.next = y; y.next = z

        #test
        self.assertEqual(func(a), True)
        self.assertEqual(func(x), False)
        print('ALL TEST PASSED')


class TestNth2EndCheck(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.a = Node(1)
        self.b = Node(2)
        self.c = Node(3)
        self.d = Node(4)
        self.e = Node(5)
        self.f = Node(6)

        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e
        self.e.next = self.f

    def test(self, func):
        self.assertRaises(LookupError, func, 7, self.a)
        self.assertEqual(func(6, self.a), 1)
        self.assertEqual(func(5, self.a), 2)
        self.assertEqual(func(4, self.a), 3)
        self.assertEqual(func(3, self.a), 4)
        self.assertEqual(func(2, self.a), 5)
        self.assertEqual(func(1, self.a), 6)
        self.assertRaises(LookupError, func, 0, self.a)
        return 'ALL TEST CASES PASSED'


class TestRecursionSum(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.times = randint(1, 100)

    def test(self, func):
        for i in range(self.times):
            value = randint(0, 300)
            self.assertEqual(func(value), sum(range(value + 1)))
        return 'ALL TEST CASES PASSED'


class TestRecurstionStringReverse(unittest.TestCase):

    def test(self, func):
        self.assertEqual(func('hello'), 'olleh')
        self.assertEqual(func('l'), 'l')
        self.assertEqual(func('follow'), 'wollof')
        self.assertEqual(func(''), '')
        return 'ALL TEST CASES PASSED'


class TestPalindromePhraseCheck(unittest.TestCase):

    def test(self, func):
        self.assertTrue(func('kayak'))
        self.assertTrue(func('aibohphobia'))
        self.assertTrue(func('Live not on evil'))
        self.assertTrue(func('Reviled did I live, said I, as evil I did deliver'))
        self.assertTrue(func('Go hang a salami; I’m a lasagna hog.'))
        self.assertTrue(func('Able was I ere I saw Elba'))
        self.assertTrue(func('Kanakanak'))
        self.assertTrue(func('Wassamassaw'))
        return 'ALL TEST CASES PASSED'

