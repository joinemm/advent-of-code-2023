import unittest

from solution import part1, part2


class Tests(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(part1("example1"), 4361)

    def test_part2_example(self):
        self.assertEqual(part2("example1"), 467835)

    def test_part1(self):
        self.assertEqual(part1("input"), 539637)

    def test_part2(self):
        self.assertEqual(part2("input"), 82818007)


if __name__ == "__main__":
    unittest.main()
