import unittest
from Student_Repository_Himanshu import Student, Instructor, University
from typing import List
""" testing different files """

class StudentTest(unittest.TestCase):
    """ Class to check class Student """
    def test_student(self) -> None:
        """ Function that tests class Student """
        actual: list = list()
        for student in University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment")._students.values():            
            actual.append(student.student_info())
        expected: List[List[str, str, List[str], List[str], List[str], float]] =  \
            [('10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44)
            ,('10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81),
            ('10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88),
            ('10175', 'Erickson, D', 'SFEN', ['SSW 564','SSW 567','SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58),
            ('10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0),
            ('11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0),
            ('11461',  'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92),
            ('11658','Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0),
            ('11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0),
            ('11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0)
            ]
        
        # test1: University = University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment")
        # print(actual)
        self.assertEqual(actual, expected)

        # with self.assertRaises(ValueError): # raises exception error
        #     Student('123', 'him', 'se').store_course_grade('SSW 810', '')

class InstructorTest(unittest.TestCase):
    """ Class to check class Instructor """
    def test_instructor(self) -> None:
        """ Function that tests class Instructor """
        actual: list = list()
        for instructor in University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment")._instructors.values():
            for c in instructor._courses:
                actual.append([instructor._cwid, instructor._name, instructor._major, c, instructor._courses[c]])
        expected: List[List[str, str, str, str, int]] = [['98765', 'Einstein, A','SFEN','SSW 567', 4],
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

class MajorTest(unittest.TestCase):
    """ Class to check class Major """
    def test_major(self) -> None:
        """ Function that tests class Major """
        actual: list = list()
        for major in University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment")._majors.values():
            # for c in major._major:
            actual.append([major._major, major._required, major._electives])
        expected: List[List[str, List[str], List[str]]] = [['SFEN', {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'}, {'CS 501', 'CS 513', 'CS 545'}],
            ['SYEN', {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}]]
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