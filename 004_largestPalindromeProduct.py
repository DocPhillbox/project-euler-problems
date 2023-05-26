import unittest

def largest_palindrome_product(num_digit: int) -> int:
    larget_palindrome: int = 0
    upper_limit: int = 10**num_digit
    lower_limit: int = 10**(num_digit-1)
    for i in range(lower_limit, upper_limit)[::-1]:
        for j in range(lower_limit, upper_limit)[::-1]:
            if is_palindrome(i*j) and i*j > larget_palindrome:
                larget_palindrome = i*j
    
    return larget_palindrome

def is_palindrome(number: int) -> bool:
    return str(number) == str(number)[::-1]

class TestLargestPalindromeProduct(unittest.TestCase):

    def test_palindrome_product(self):
        self.assertEqual(largest_palindrome_product(2), 9009)
        self.assertEqual(largest_palindrome_product(3), 906609)

unittest.main()