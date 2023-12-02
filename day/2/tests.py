import unittest

from solution import part1, part2


class Tests(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(part1("example1"), 8)

    def test_part2_example(self):
        self.assertEqual(part2("example1"), 2286)

    def test_part1(self):
        self.assertEqual(part1("input"), 2551)

    def test_part2(self):
        self.assertEqual(part2("input"), 62811)


if __name__ == "__main__":
    unittest.main()
