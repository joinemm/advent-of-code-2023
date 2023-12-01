import unittest

from solution import part1, part2


class Tests(unittest.TestCase):
    def test_part1_example(self):
        self.assertEqual(part1("example1"), 142)

    def test_part2_example(self):
        self.assertEqual(part2("example2"), 281)

    def test_part1(self):
        self.assertEqual(part1("input"), 54990)

    def test_part2(self):
        self.assertEqual(part2("input"), 54473)


if __name__ == "__main__":
    unittest.main()
