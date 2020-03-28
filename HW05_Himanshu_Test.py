import unittest
from HW05_Himanshu import reverse_string, sub_string, find_second, get_lines
from typing import List

'''testing all types of cases'''

class GetLinesTest(unittest.TestCase):
    ''' testing cases '''

    def test_reverse_string(self) -> None:
        '''testing if string is reversing or not'''
        self.assertEqual(reverse_string('Hello'), 'olleH')
        self.assertNotEqual(reverse_string('hello'), 'hello')
        self.assertEqual(reverse_string(' hello '), ' olleh ')
        self.assertNotEqual(reverse_string(' '), 'olleh')
        self.assertEqual(reverse_string(''), '')

        with self.assertRaises(ValueError):
            reverse_string(66756)

    def test_sub_string(self) -> None:
        '''testing if string is reversing or not'''
        self.assertEqual(sub_string('he', 'hello'), 0)
        self.assertEqual(sub_string('ab', 'abbabba'), 0)
        self.assertEqual(sub_string('123', 'hello'), -1)
        self.assertNotEqual(sub_string('mis', 'mississppi'), -1)
        self.assertEqual(sub_string('', 'hello'), 0)

        a: str = 'hello'
        self.assertTrue(sub_string('he', 'hello') == a.find('he'))
        self.assertFalse(sub_string('he', 'hello') != a.find('he'))

    def test_find_second(self) -> None:
        '''testing if string is reversing or not'''
        self.assertEqual(find_second('he', 'hello'), -1)
        self.assertEqual(find_second('123', 'hello'), -1)
        self.assertEqual(find_second('ab', 'abbacca'), -1)
        self.assertEqual(find_second('iss', 'mississppi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertNotEqual(find_second(' ', 'hello'), 8)

    def test_get_lines(self) -> None:
        '''getting lines from a file'''
        with self.assertRaises(FileNotFoundError):
            list(get_lines('file not found'))
            
        file_name: str = 'test1.txt'
        expect1: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        expect2: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5># comment', '<line6>']
        expect3: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>', '','<line4.1 line4.2>', '<line5>', '<line6>']
        result: List[str] = list(get_lines(file_name))

        self.assertEqual(result, expect1)
        self.assertNotEqual(result, expect2)
        self.assertNotEqual(result, expect3)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)