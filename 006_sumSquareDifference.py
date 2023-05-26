import unittest

def sum_square_difference(limit: int):
    total: int = 0
    total_squarred: int = 0
    for i in range(limit):
        total += i + 1
        total_squarred += (i + 1) ** 2

    return total ** 2 - total_squarred

class TestSumSquareDifference(unittest.TestCase):

    def test_sum_square(self):
        self.assertEqual(sum_square_difference(10), 2640)
        self.assertEqual(sum_square_difference(20), 41230)
        self.assertEqual(sum_square_difference(100), 25164150)

unittest.main()