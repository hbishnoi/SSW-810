"""Python code to read files, Analyze them using python and basic Date time Airthmatic"""
from datetime import datetime, timedelta
from typing import Tuple, IO, Iterator, Dict
import os
from prettytable import PrettyTable

def date_arithmetic()-> Tuple[datetime, datetime, int]:
    """ perfoming arithmetic operation on dates """
    date1: str = 'February 27, 2020'
    date2: str = 'February 27, 2019'
    date3: str = 'February 1, 2019'
    date4: str = 'September 30, 2019'
    NUM_DAYS: int = 3

    dt1: datetime = datetime.strptime(date1, '%B %d, %Y')
    dt2: datetime = datetime.strptime(date2, '%B %d, %Y')
    dt3: datetime = datetime.strptime(date3, '%B %d, %Y')
    dt4: datetime = datetime.strptime(date4, '%B %d, %Y')

    three_days_after_02272000: datetime = dt1 + timedelta(days=NUM_DAYS)
    three_days_after_02272017: datetime = dt2 + timedelta(days=NUM_DAYS)
    days_passed_01012017_10312017: datetime = dt4 - dt3

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017.days

# print(date_arithmetic())


def file_reader(path: str, fields: int, sep = ',', header = False) -> Iterator[Tuple[str]]:
    """ reading all the fields in a file using generator """
    try:
        fp: IO = open(path, 'r', encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can not open {path}")
        # print (f"Can not open {path}")
    else:
        with fp:
            for offset, line in enumerate(fp, 1):
                current_line: list = line.rstrip('\n').split(sep)
                if len(current_line) != fields:
                    raise ValueError(f"{fp} has {len(current_line)} fields on line {offset} but expected {fields}")
                elif offset == 1 and header:
                    continue
                else:
                    yield tuple(current_line)

# print(list(file_reader("student_majors.txt", 3, sep='|', header=True)))


class FileAnalyzer:
    """ implement analyze_filers, pretty_print functions in this class """

    def __init__(self, directory) -> None:
        """ initalizes variable directory """
        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()

    def analyze_files(self) -> None:
        """ count number of lines, characters, functions and classes """
        try:
            list_files: list = os.listdir(self.directory)
        except FileExistsError:
            raise FileExistsError("files not found or directory is not correct")
        else:
            for file_name in list_files:
            # for file in os.listdir(self.directory):
                if file_name.endswith(".py"):
                    try:
                        fp: IO = open(os.path.join(self.directory, file_name), "r")
                    except FileNotFoundError:
                        raise FileNotFoundError(f"Can't open the file")
                    else:
                        with fp:
                            count_lines: int = 0
                            count_char: int = 0
                            count_func: int = 0
                            count_class: int = 0
                            for line in fp:        
                                count_char += len(line)         
                                line: str = line.strip()
                                count_lines += 1
                                if line.startswith("def ") and line.endswith(":"): 
                                    count_func += 1
                                elif line.startswith("class ") and line.endswith(":"):
                                    count_class += 1
                        self.files_summary[file_name] = {"class": count_class, "function": count_func, "line": count_lines, "char": count_char}
        # return self.files_summary
            
    def pretty_print(self) -> None:
        """ printing the table using pretty table """
        pretty_table: PrettyTable = PrettyTable(field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"])

        for file_name in self.files_summary:
            pretty_table.add_row([file_name, self.files_summary[file_name]["class"], self.files_summary[file_name]["function"], \
                self.files_summary[file_name]["line"], self.files_summary[file_name]["char"]])
        return pretty_table