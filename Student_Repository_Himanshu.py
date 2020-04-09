import os
from collections import defaultdict
from prettytable import PrettyTable
from typing import DefaultDict, Dict, Tuple, List, Iterator, Set
from HW08_Himanshu import file_reader

class Student:
    """ Store everything about a single student """
    pt_hdr: List[str] = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Required', 'Remaining Electives', 'GPA'] 

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """ store every info about a student """
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._course: Dict[str, str] = dict()
        self._remaining_required = list()
        self._remaining_electives = list()
        self._gpa: float = 0.0 

    def store_course_grade(self, course: str, grade:str) -> None:
        """ store grade with respect to course student has taken """
        if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']:
            self._course[course] = grade
        elif grade in ['C-', 'D+', 'D', 'D-', 'F']:
            print(f'Student with CWID {self._cwid} has failed this course.')
        else:
            print(f'Student with CWID {self._cwid} has no record with this course.')
        # print(self._course)

        if len(self._course.values()) > 0 :
            grade_point: Dict[str,float] = {'A' : 4.0, 'A-' : 3.75, 'B+' : 3.25, 'B' : 3.0, 'B-' : 2.75, 'C+' : 2.25, \
                'C' : 2.0, 'C-' : 0, 'D+' : 0, 'D' : 0,'D-' : 0, 'F' : 0}
            self._gpa = round(sum([grade_point[grade] for grade in self._course.values()])/len(self._course.values()), 2)
            
    def student_info(self) -> Tuple[str, str, List[str], List[str], List[str], float]:
        """ return information needed for student pretty table """
        # req, elec = Major(self._course).course_remaining()
        remain_req, remain_elec = Major(self._course).course_remaining(self._course)
        # req = Major(self._course).course_remaining()
        # elec = Major(self._course).course_remaining()
        return self._cwid, self._name, self._major, sorted(self._course.keys()), remain_req, remain_elec, self._gpa

class Instructor:
    """Store instructor inforamtion"""
    pt_hdr: List[str] = ['CWID', 'Name', 'Dept', 'Course', 'Students']

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

class Major:
    """Store major information"""
    pt_hdr: List[str] = ['Major', 'Required Courses', 'Electives']
    valid_grade = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']

    def __init__(self, major: str) -> None:
        """ store every info about a major """
        self._major: str = major
        self.valid_grade
        self._required: List[str] = list()
        self._electives: List[str] = list()

    def add_course(self, course_type: str, course: str) -> List:
        """ add course to their respective category """
        if course_type.upper() == 'R':
            self._required.append(course)
        elif course_type.upper() == 'E':
            self._electives.append(course)
        else:
            print(f"Unknown type {course_type} found.")
    
    def course_remaining(self, course: str):
        ''' to test if the student passed the course or not and return:
            the major, completed courses, remaining required and elective courses 
        '''
        completed_courses: List[str] = set()
        for course, grade in course.items():
            if grade in Major.valid_grade:
                completed_courses.add(course)

        remaining_req = set(self._required) - completed_courses
        remaining_elec = set(self._electives) - completed_courses

        if len(remaining_elec) < len(self._electives):
            remaining_elec = {None}

        return remaining_req, remaining_elec

    # def course_remaining(self,) -> List:
    #     """ adding remaining course that should be taken by students """
    #     # req: List[str] = list()
    #     # elect: List[str] = list()
    #     # completed_courses = set()
    #     remaining_required = self._required.copy()
    #     remaining_elective = self._electives.copy()

        
    #     if self._major in remaining_required:
    #         remaining_required.remove(self._major)
    #     elif self._major in remaining_elective:
    #         remaining_elective = list() #empty list
        
        # for course in self._major.keys():
        #     # if grade in self.valid_grade:
        #     # completed_courses.add(course)
        #     if course in self._electives:
        #         remaining_elective = None
            
        #     if course in self._required:
        #         remaining_required.remove(course)
        
        # return remaining_required, remaining_elective
        # return(set(self._required), set(self._electives))

        # x = list()
        # for course in self._major.keys():
        #     x.append(course)
        # rem_r = set(self._required) - set(x)
        # re = set(self._electives)

        # if re.intersection(set(x)):
        #     rem_ele = None
        # else:
        #     rem_ele = re

        # return rem_r, rem_ele

        
        # for course in self._required:
        #     if self._major != course:
        #         req.append(self._required)
        #     elif self._major != self._electives:
        #         elect.append(self._electives)
        #     else:
        #         pass
    
    def major_info(self) -> Tuple[str, str, str]:
        """ return information needed for instructor pretty table """
        return self._major, sorted(self._required), sorted(self._electives)

class University:
        """ Repository to store students instructors for university and print pretty table """

        def __init__(self, path: str)->None:
            """ store students, instructors and pretty table """
            self._path = path
            self._students: Dict[str, Student] = dict()
            self._instructors: Dict[str, Instructor] = dict()
            self._majors: Dict[str, Major] = dict()
            self._read_students()
            self._read_instructors()
            self._read_grades()
            self._read_majors()
            
        def _read_students(self) -> None:
            """ read student file and assigning values to dictionary """
            try:
                directory: str = os.path.join(self._path, 'students.txt')
            except(FileNotFoundError) as e:
                print(e)
            else:
                for cwid, name, major in file_reader(directory, 3, sep = ';', header = True):
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
                for cwid, name, major in file_reader(directory, 3, sep = '|', header = True):
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
                for student_cwid, course, grade, instructor_cwid in file_reader(directory, 4, sep = '|', header = True):
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

        def _read_majors(self) -> None:
            """ read grades file and assigning values to dictionary """
            try:
                directory: str = os.path.join(self._path, 'majors.txt')
            except(FileNotFoundError) as e:
                print(e)
            else:
                for major, r_e, course in file_reader(directory, 3, sep = '\t', header = True):
                    if major not in self._majors.keys():         
                        # self._majors[major] = Major(major, r_e, course)
                        self._majors[major] = Major(major)
                    self._majors[major].add_course(r_e, course)

        def major_prettytable(self):
            """Sends the major data to the pretty table and prints it"""
            pretty_table3: PrettyTable = PrettyTable(field_names=Major.pt_hdr)
            for values in self._majors.values():
                pretty_table3.add_row(values.major_info())
            print(pretty_table3)
 
        def student_prettytable(self):
            """Sends the student data to the pretty table and prints it"""
            pretty_table1: PrettyTable = PrettyTable(field_names=Student.pt_hdr)
            for student in self._students.values():
                print(student.student_info())     
                pretty_table1.add_row(student.student_info())
            print(pretty_table1)
 
        def instructor_prettytable(self):
            """Sends the instructors data to the pretty table and prints it"""
            pretty_table2: PrettyTable = PrettyTable(field_names=Instructor.pt_hdr)
            for instructor in self._instructors.keys():
                for c in self._instructors[instructor].instructor_info():
                    pretty_table2.add_row(c)
            print(pretty_table2)
            
        
def main():
    """ define the repositiry  """
    stevens: University = University("C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment")
    # nyu: University = University("put the path in here").
    stevens.major_prettytable()
    stevens.student_prettytable()
    stevens.instructor_prettytable()

if __name__ == "__main__":
    main()