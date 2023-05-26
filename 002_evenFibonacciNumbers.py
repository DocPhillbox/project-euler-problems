import unittest

def even_fibonacci_numbers(number: int) -> int:
    fib_list: list[int] = []
    for i in range(number):
        fib_list.append(fibonacci(i+1))
    
    total: int = 0
    for sequ in fib_list:
        if sequ % 2 == 0:
            total += sequ
    
    return total

def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)


class TestEvenFibonaciiNumbers(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(even_fibonacci_numbers(10) % 2 == 0)
        self.assertTrue(even_fibonacci_numbers(20) % 2 == 0)
    
    def test_fibonacci_sequence(self):
        self.assertEqual(even_fibonacci_numbers(8), 10)
        self.assertEqual(even_fibonacci_numbers(10), 44)
        self.assertEqual(even_fibonacci_numbers(15), 798)

unittest.main()