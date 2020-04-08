'''testing all the methods which includes all types of containers'''
import unittest
from datetime import datetime, timedelta
from HW08_Himanshu import date_arithmetic, file_reader, FileAnalyzer

class TestModuleGeneratorFile(unittest.TestCase):
    """ Class to perform unit test   """

    def test_date_arithmetic(self):
        """  Unit Testing for date_arithmetic """
        self.assertEqual(date_arithmetic(), (datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 241))
        self.assertNotEqual(date_arithmetic(), (datetime(2000, 4, 1, 0, 0), datetime(2017, 3, 2, 0, 0), 254))
        self.assertNotEqual(date_arithmetic(), '')


    def test_file_reader(self):
        """  Unit Testing for file_reader """
        a = list(file_reader("student_majors.txt", 3, sep='|', header=True))

        b = [('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'), \
            ('345', 'Benji Cai', 'Software Engineering')]
        self.assertEqual(a, b)
        
        c = [("CWID", "Name", "Major"), ('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'), \
            ('345', 'Benji Cai', 'Software Engineering')]
        self.assertNotEqual(a,c)


    def test_file_analyzer(self):
        """Test cases for file analyser"""
        file_analyzer = FileAnalyzer("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment 8")
        self.assertEqual(file_analyzer.files_summary, {'HW08_Himanshu.py': {'class': 1, 'function': 5, 'line': 100, 'char': 4472}, \
            'HW08_Test_Himanshu.py': {'class': 1, 'function': 3, 'line': 38, 'char': 1861}})
        self.assertNotEqual(file_analyzer.files_summary, {'HW08_Himanshu.py': {'class': 0, 'function': 5, 'line': 46, 'char': 1931}})

        self.assertNotEqual(file_analyzer.files_summary, {'HW08_Himanshu.py': {'class': 1, 'function': 5, 'line': 100}}) # testing less fields

        with self.assertRaises(FileNotFoundError): # raises exception error
            FileAnalyzer("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment 10").files_summary

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)