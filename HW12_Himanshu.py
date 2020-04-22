from flask import Flask, render_template
import sqlite3
from typing import Dict

"""using html form with flask and python"""

app: Flask = Flask(__name__)

DB_FILE: str = "C:\\Users\\Himan\\Desktop\\Semester 2\\SSW 810\\HW\\Assignment 11\\HW11_db"

@app.route('/HW12')
def completed_courses():
    """extract data from database and send it to front end to show it on browser"""
    
    try:
        db: sqlite3.Connection = sqlite3.connect(DB_FILE)
    except sqlite3.OperationalError as e:
        print(e)
    else:
        query: str = """select students.Name as Student_Name, students.CWID, grades.Course, grades.Grade, instructors.Name as Instructor_Name \
                    from ((students inner join grades on students.CWID = grades.StudentCWID) \
                    inner join instructors on grades.InstructorCWID = instructors.CWID) order by Student_Name ASC"""

        data: Dict[str, str] = \
            [{"name": name, "cwid": cwid, "major": major, "grade": grade, "instructor": instructor} 
                for name, cwid, major, grade, instructor in db.execute(query)]

        db.close()

    return render_template(
        'students_summary.html',
        title="Stevens Repository",
        table_title="Students courses and grade",
        students=data)


app.run(debug=True)