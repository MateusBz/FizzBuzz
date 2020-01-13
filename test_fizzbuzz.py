#!/usr/bin/env python3

import unittest
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz.fizzbuzz(6), 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(20), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'FizzBuzz')

    def test_regular_numbers(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz.fizzbuzz(82), 82)


if __name__ == '__main__':
    unittest.main()

