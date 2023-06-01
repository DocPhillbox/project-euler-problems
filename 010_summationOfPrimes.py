import unittest


def summation_of_primes(limit: int) -> int:
    sum: int = 0
    for i in range(1, limit):
        if is_prime(i):
            sum += i

    return sum


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


class TestSummationOfPrimes(unittest.TestCase):
    def test_summation(self):
        self.assertEqual(summation_of_primes(17), 41)
        self.assertEqual(summation_of_primes(2001), 277050)
        self.assertEqual(summation_of_primes(140759), 873608362)
        self.assertEqual(summation_of_primes(2000000), 142913828922)


unittest.main()
