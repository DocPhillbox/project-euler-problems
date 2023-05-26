import unittest


def multiple_of_3_and_5(number: int) -> int:
    total: int = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


class TestMultipleOf3And5(unittest.TestCase):
    def test_multiples(self):
        self.assertEqual(543, multiple_of_3_and_5(49))
        self.assertEqual(233168, multiple_of_3_and_5(1000))
        self.assertEqual(16687353, multiple_of_3_and_5(8456))
        self.assertEqual(89301183, multiple_of_3_and_5(19564))


unittest.main()
