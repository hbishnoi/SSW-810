import unittest
from HW09_Himanshu import Student, Instructor, University
from typing import List
""" testing different files """

class StudentTest(unittest.TestCase):
    """ Class to check class Student """
    def test_student(self) -> None:
        """ Function that tests class Student """
        actual: list = list()
        for student in University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment 1")._students.values():            
            actual.append([student._cwid, student._name, sorted(student._course.keys())])
        expected: List[List[str, str, List[str]]] =  [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
            ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
            ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
            ['10175', 'Erickson, D', ['SSW 564','SSW 567','SSW 687']],
            ['10183', 'Chapman, O', ['SSW 689']],
            ['11399', 'Cordova, I', ['SSW 540']],
            ['11461',  'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']],
            ['11658','Kelly, P', ['SSW 540']],
            ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
            ['11788', 'Fuller, E', ['SSW 540']]]
        # test1: University = University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment 1")
        # print(actual)
        self.assertEqual(actual, expected)

        with self.assertRaises(ValueError): # raises exception error
            Student('123', 'him', 'se').store_course_grade('SSW 810', '')
        
class InstructorTest(unittest.TestCase):
    """ Class to check class Instructor """
    def test_instructor(self) -> None:
        """ Function that tests class Instructor """
        actual: list = list()
        for instructor in University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment 1")._instructors.values():
            for c in instructor._courses:
                actual.append([instructor._cwid, instructor._name, instructor._major, c, instructor._courses[c]])
        expected: List[List[str, str, List[str]]] = [['98765', 'Einstein, A','SFEN','SSW 567', 4],
            ['98765', 'Einstein, A','SFEN','SSW 540', 3],
            ['98764', 'Feynman, R','SFEN','SSW 564', 3],
            ['98764', 'Feynman, R','SFEN','SSW 687', 3],
            ['98764', 'Feynman, R','SFEN','CS 501', 1],
            ['98764', 'Feynman, R','SFEN','CS 545', 1],
            ['98763', 'Newton, I','SFEN','SSW 555', 1],
            ['98763', 'Newton, I','SFEN','SSW 689', 1],
            ['98760', 'Darwin, C','SYEN','SYS 800', 1],
            ['98760', 'Darwin, C','SYEN','SYS 750', 1],
            ['98760', 'Darwin, C','SYEN','SYS 611', 2],
            ['98760', 'Darwin, C','SYEN','SYS 645', 1]]
        self.assertEqual(actual, expected)

class ErrorTest(unittest.TestCase):
    """ testing all the errors """
    def test_error_student(self) -> None:
        """ Function that tests Student file not found error """
        with self.assertRaises(FileNotFoundError): # raises exception error
            University("nothing to check")._read_students()
    
    def test_error_instructor(self) -> None:
        """ Function that tests Instructor file not found error """
        with self.assertRaises(FileNotFoundError): # raises exception error
            University("nothing to check")._read_instructors()
    
    def test_error_grades(self) -> None:
        """ Function that tests Grades file not found error """
        with self.assertRaises(FileNotFoundError): # raises exception error
            University("nothing to check")._read_grades()

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)