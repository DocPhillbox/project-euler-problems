import unittest


def find_nth_prime(limit: int) -> int:
    count: int = 1
    i: int = 1
    while count <= limit:
        i += 1
        if is_prime(i):
            count += 1

    return i


def is_prime(number: int) -> bool:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


class TestFindNthPrime(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(find_nth_prime(6), 13)
        self.assertEqual(find_nth_prime(10), 29)
        self.assertEqual(find_nth_prime(100), 541)
        self.assertEqual(find_nth_prime(1000), 7919)
        self.assertEqual(find_nth_prime(10001), 104743)


unittest.main()
