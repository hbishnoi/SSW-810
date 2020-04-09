import os
from collections import defaultdict
from prettytable import PrettyTable
from typing import DefaultDict, Dict, Tuple, List, Iterator
from HW08_Himanshu import file_reader

class Student:
    """ Store everything about a single student """

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """ store every info about a student """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._course: Dict[str, str] = dict()

    def store_course_grade(self, course: str, grade:str) -> None:
        """ store grade with respect to course student has taken """
        if grade != '':
            self._course[course] = grade
        else:
            raise ValueError("Grade is empty !!!")
        # print(self._course)

    def student_info(self) -> Tuple[str, str, List[str]]:
        """ return information needed for student pretty table """
        return self._cwid, self._name, sorted(self._course.keys())

class Instructor:
    """Store instructor inforamtion"""

    def __init__(self, cwid: str, name:str, major:str ) -> None:
        """ store every info about a instructor """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        # self._courses: DefaultDict[str, str] = defaultdict(int)
        self._courses: DefaultDict[str, int] = defaultdict(int)
    
    def store_course_students(self, course: str) -> None:
        """ counting how many students are in a particular course instructor is taking """
        self._courses[course] += 1
        
    def instructor_info(self) -> Iterator[Tuple[str, str, str, str, int]]:
        """ return information needed for instructor pretty table """
        # list_inst: list = list()
        for course, student_number in self._courses.items():
            # list_inst.append([self._cwid, self._name, self._major, course, student_number])
            yield self._cwid, self._name, self._major, course, student_number
        # return list_inst

class University:
        """ Repository to store students instructors for university and print pretty table """

        def __init__(self, path: str)->None:
            """ store students, instructors and pretty table """
            self._path = path
            self._students: Dict[str, Student] = dict()
            self._instructors: Dict[str, Instructor] = dict()
            self._read_students()
            self._read_instructors()
            self._read_grades()
            
        def _read_students(self) -> None:
            """ read student file and assigning values to dictionary """
            try:
                directory: str = os.path.join(self._path, 'students.txt')
            except(FileNotFoundError) as e:
                print(e)
            else:
                for cwid, name, major in file_reader(directory, 3, sep = '\t', header = False):
                    self._students[cwid] = Student(cwid, name, major)
                    # return self._students
                    # print(self._students)
            
        def _read_instructors(self) -> None:
            """ read instructor file and assigning values to dictionary """
            try:
                directory: str = os.path.join(self._path, 'instructors.txt')
            except(FileNotFoundError) as e:
                print(e)
            else:
                for cwid, name, major in file_reader(directory, 3, sep = '\t', header = False):
                    self._instructors[cwid] = Instructor(cwid, name, major)
                    # print(self._instructors)
                    # return self._instructors

        def _read_grades(self) -> None:
            """ read grades file and assigning values to dictionary """
            try:
                directory: str = os.path.join(self._path, 'grades.txt')
            except(FileNotFoundError) as e:
                print(e)
            else:
                for student_cwid, course, grade, instructor_cwid in file_reader(directory, 4, sep = '\t', header = False):
                    if student_cwid in self._students.keys():
                        self._students[student_cwid].store_course_grade(course, grade)
                        # return grade
                    else:
                        raise ValueError(f"student with id: {student_cwid} is not matched with any data")

                    if instructor_cwid in self._instructors.keys():
                        self._instructors[instructor_cwid].store_course_students(course)
                        # return self._instructors
                    else:
                        raise ValueError(f"professor with id: {instructor_cwid} is not matched with any data")

        def student_prettytable(self):
            """Sends the student data to the pretty table and prints it"""
            pretty_table1: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
            for student in self._students.values():            
                pretty_table1.add_row(student.student_info())
            print(pretty_table1)
 
        def instructor_prettytable(self):
            """Sends the instructors data to the pretty table and prints it"""
            pretty_table2: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
            for instructor in self._instructors.keys():
                for c in self._instructors[instructor].instructor_info():
                    pretty_table2.add_row(c)
            print(pretty_table2)
            
        
# def main():
#     """ define the repositiry  """
#     stevens: University = University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment")
#     # nyu: University = University("put the path in here").
#     stevens.student_prettytable()
#     stevens.instructor_prettytable()

# if __name__ == "__main__":
#     main()
