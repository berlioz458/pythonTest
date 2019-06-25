import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-15), 15, "Should be absolute value of a number")

    def test_abs3(self):
        self.assertEqual(abs(-8), -8, "Should be absolute value of a number")

    def test_abs4(self):
        self.assertEqual(abs(-99), 99, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()
