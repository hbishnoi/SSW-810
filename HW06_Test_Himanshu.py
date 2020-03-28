'''importing everything we need for the testing'''
import unittest
from HW06_Himanshu import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, DonutQueue

'''testing all types of cases'''

class GetLinesTest(unittest.TestCase):
    ''' testing cases '''

    def test_list_copy(self) -> None:
        '''testing if list is making a new copy or not'''
        self.assertEqual(list_copy(['Hello', 123]), ['Hello', 123])
        self.assertNotEqual(list_copy(['Hello', 123]), [123, 'Hello'])
        self.assertEqual(list_copy([]), [])

    def test_list_intersect(self) -> None:
        '''testing if two list have any common elements'''
        self.assertEqual(list_intersect([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
        self.assertNotEqual(list_intersect([1, 2, 3, 4], [5, 6]), [3, 4])
        self.assertEqual(list_intersect([1, 2, 3, 4], [5, 6]), [])
        self.assertEqual(list_intersect([], [5, 6]), [])
        self.assertEqual(list_intersect([], []), [])

    def test_list_difference(self) -> None:
        '''testing if first list have any element which is not common with second list'''
        self.assertEqual(list_difference(['Hello', 123], [123]), ['Hello'])
        self.assertNotEqual(list_difference(['Hello', 123], [123]), [123])
        self.assertEqual(list_difference([1, 2, 3], [4, 5, 6]), [1, 2, 3])
        self.assertEqual(list_difference([1, 2], [1, 2, 3, 4, 5, 6]), [])

    def test_remove_vowels(self) -> None:
        '''testing if function removes the words which starts with any vowels'''
        self.assertEqual(remove_vowels('hello I am Himanshu'), 'hello Himanshu')
        self.assertNotEqual(remove_vowels('hello I am Himanshu'), 'hello I Himanshu')
        self.assertEqual(remove_vowels('a e i o u'), '')

    def test_check_pwd(self) -> None:
        '''testing if password starts with digit, have one lower caseletter and two uppercase letter'''
        self.assertEqual(check_pwd('1HWello'), True)
        self.assertEqual(check_pwd('1HWe'), True)
        self.assertEqual(check_pwd('1hello'), False)
        self.assertEqual(check_pwd('1HELLO'), False)
        self.assertEqual(check_pwd('HEllo'), False)
        self.assertEqual(check_pwd(''), False)
        # self.assertFalse(check_pwd('') is True)
        self.assertNotEqual(check_pwd('123'), True)
        self.assertNotEqual(check_pwd('HWello'), True)

class DonutQueueTest(unittest.TestCase):
    '''class for donut queue where we have normal customers and priority customers'''
    def test_queue(self):
         dq = DonutQueue()
         self.assertIsNone(dq.next_customer())
         dq.arrive("Sujit", False)
         dq.arrive("Fei", False)
         dq.arrive("Prof JR", True)
         self.assertEqual(dq.waiting(), "Prof JR, Sujit, Fei")
         dq.arrive("Nanda", True)
         self.assertEqual(dq.waiting(), "Prof JR, Nanda, Sujit, Fei")
         self.assertEqual(dq.next_customer(), "Prof JR")
         self.assertEqual(dq.next_customer(), "Nanda")
         self.assertEqual(dq.next_customer(), "Sujit")
         self.assertEqual(dq.waiting(), "Fei")
         self.assertEqual(dq.next_customer(), "Fei")
         self.assertIsNone(dq.next_customer())

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)