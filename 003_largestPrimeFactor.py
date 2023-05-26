import unittest


def largest_prime_factor(number: int) -> int:
    primes: list[int] = compute_primes(number)
    for prime in primes[::-1]:
        if number % prime == 0:
            return prime

    return 1


def compute_primes(limit: int) -> list[int]:
    primes: list[int] = []
    for i in range(2, limit + 1):
        if is_prime(i):
            primes.append(i)

    return primes


def is_prime(number: int) -> bool:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


class TestLargestPrimeFactor(unittest.TestCase):
    def test_prime_factor(self):
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(7), 7)
        self.assertEqual(largest_prime_factor(8), 2)
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(82284), 6857)


unittest.main()
