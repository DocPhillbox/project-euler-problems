import unittest


def smallest_multiple(limit: int) -> int:
    multiple: int = 0
    is_smallest_multiple: bool = False
    while not is_smallest_multiple:
        multiple += 1
        is_smallest_multiple = True
        for i in range(limit):
            if not multiple % (i + 1) == 0:
                is_smallest_multiple = False

    return multiple


class TestSmallestMultiple(unittest.TestCase):
    def test_smallest_multiple(self):
        self.assertEqual(smallest_multiple(5), 60)
        self.assertEqual(smallest_multiple(7), 420)
        self.assertEqual(smallest_multiple(10), 2520)
        self.assertEqual(smallest_multiple(13), 360360)


unittest.main()
