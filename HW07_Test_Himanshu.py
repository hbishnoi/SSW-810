'''testing all the methods which includes all types of containers'''
import unittest
from HW07_Himanshu import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer
from typing import List, Tuple

class GetLinesTest(unittest.TestCase):
    '''test class'''
    def test_anagrams_lst(self):
        '''testing two string if they are anagrams or not'''
        self.assertEqual(anagrams_lst('dormitory', 'Dirtyroom'), True)
        self.assertEqual(anagrams_lst('Dormitory', 'dirtyroom'), True)
        self.assertEqual(anagrams_lst('dormitory', ''), False)
        self.assertEqual(anagrams_lst('', 'Dirtyroom'), False)
        self.assertEqual(anagrams_lst('121', '211'), True)
        self.assertNotEqual(anagrams_lst('dormitory', ''), True)
        self.assertEqual(anagrams_lst('', ''), True)
    
    def test_anagrams_dd(self):
        '''testing two string if they are anagrams or not using defaultdict'''
        self.assertEqual(anagrams_dd('dormitory', 'Dirtyroom'), True)
        self.assertEqual(anagrams_dd('Dormitory', 'dirtyroom'), True)
        self.assertEqual(anagrams_dd('dormitory', ''), False)
        self.assertEqual(anagrams_dd('', 'Dirtyroom'), False)
        self.assertEqual(anagrams_dd('121', '211'), True)
        self.assertNotEqual(anagrams_dd('dormitory', ''), True)
        self.assertEqual(anagrams_dd('', ''), True)
    
    def test_anagrams_cntr(self):
        '''testing two string if they are anagrams or not using counter'''
        self.assertEqual(anagrams_cntr('dormitory', 'Dirtyroom'), True)
        self.assertEqual(anagrams_cntr('Dormitory', 'dirtyroom'), True)
        self.assertEqual(anagrams_cntr('dormitory', ''), False)
        self.assertEqual(anagrams_cntr('', 'Dirtyroom'), False)
        self.assertEqual(anagrams_cntr('121', '211'), True)
        self.assertNotEqual(anagrams_cntr('dormitory', ''), True)
        self.assertEqual(anagrams_cntr('', ''), True)

    def test_covers_alphabet(self):
        '''testing if the string contains all the alphabets'''
        self.assertEqual(covers_alphabet('We promptly judged antique ivory buckles for the next prize'), True)
        self.assertEqual(covers_alphabet('The quick, brown, fox; jumps over the lazy dog!'), True)
        self.assertEqual(covers_alphabet('dormitory'), False)
        self.assertEqual(covers_alphabet(''), False)
        self.assertEqual(covers_alphabet('121'), False)
        self.assertNotEqual(covers_alphabet('dormitory'), True)
        self.assertEqual(covers_alphabet('aabbcdefghijklmnopqrstuvwxyzzabc'), True)
        self.assertEqual(covers_alphabet('abcdefghijklmnopqrstuvwxyz'), True)
    
    def test_web_analyzer(self):
        '''testing list which includes tuples are correctly in ascending order'''
        weblogs: List[Tuple[str, str]] = [
        ('Nanda', 'google.com'), ('Maha', 'google.com'), 
        ('Fei', 'python.org'), ('Maha', 'google.com'), 
        ('Fei', 'python.org'), ('Nanda', 'python.org'), 
        ('Fei', 'dzone.com'), ('Nanda', 'google.com'), 
        ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
        ('dzone.com', ['Fei']), 
        ('google.com', ['Maha', 'Nanda']), 
        ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary, True)
        self.assertNotEqual(web_analyzer(weblogs), [], True)
        self.assertEqual(web_analyzer([]), [], True)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)