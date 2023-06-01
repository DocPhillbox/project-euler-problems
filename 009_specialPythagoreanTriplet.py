import unittest


def special_pythagorean_triplet(number: int) -> list[int]:
    pythagorean_triplet: list[int] = []
    for a in range(1, number):
        for b in range(a, number):
            c: int = number - a - b
            if a**2 + b**2 == c**2:
                pythagorean_triplet.append(a * b * c)
    return pythagorean_triplet


class TestPythagoreanTriplet(unittest.TestCase):
    def test_triplet(self):
        self.assertEqual(special_pythagorean_triplet(24), [480])
        self.assertEqual(special_pythagorean_triplet(120), [49920, 55080, 60000])
        self.assertEqual(special_pythagorean_triplet(1000), [31875000])


unittest.main()
