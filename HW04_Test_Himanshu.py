'''testing count vowels, occurrence of a char and enumerate function'''
import unittest
from HW04_Himanshu import count_vowels, last_occurrence, my_enumerate

class CountVowelsTest(unittest.TestCase):
    '''test class'''

    def test_count_vowels(self) -> None:
        '''testing how many vowels are in a string'''
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('aeiouAEIOU'), 10)
        self.assertEqual(count_vowels('why'), 0)
        self.assertEqual(count_vowels('hEllO world'), 3)
        # self.assertEqual(count_vowels(66756), None)
        with self.assertRaises(ValueError):
            count_vowels(66756)
            # count_vowels('.')
        self.assertNotEqual(count_vowels('why'), count_vowels('hello'))
        self.assertEqual(count_vowels(''), 0)

    def test_last_occurrence(self) -> None:
        '''testing the last occurrence of a target value in a string'''
        self.assertEqual(last_occurrence('p', 'apple'), 2)
        self.assertEqual(last_occurrence('p', 'orange'), None)
        self.assertNotEqual(last_occurrence('p', 'apple'), 0)
        self.assertEqual(last_occurrence(5, 'apple'), None)
        self.assertEqual(last_occurrence('', 'apple'), None)
        self.assertEqual(last_occurrence('5', 'apple'), None)
        self.assertEqual(last_occurrence('A', 'Aapple'), 0)
        self.assertEqual(last_occurrence(33,[33,21,33,23,33]),4)

    def test_my_enumerate(self) -> None:
        '''testing in built enumerate function'''
        self.assertEqual(list(my_enumerate('hello world')), list(enumerate('hello world')))
        self.assertNotEqual(list(my_enumerate('hello world')), list(enumerate('why')))
        self.assertNotEqual(list(my_enumerate('')), list(enumerate('hello world')))
        self.assertNotEqual(list(my_enumerate([5, 4, 6])), list(enumerate('hello world')))
        self.assertEqual(list(my_enumerate([5, 4, 6])), list(enumerate([5, 4, 6])))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)