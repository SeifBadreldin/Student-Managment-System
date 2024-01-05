from utility import *

def Generate_Results():
    courses = ReadJson('courses.json')
    students = ReadJson('students.json')
    for student_info in students.items():
        with open(f"{student_info['Student Code']}.html", 'w') as f:
            f.write('<!DOCTYPE html>\n')
            f.write('<html>\n')
            f.write('<head>\n')
            f.write('<link rel="stylesheet" type="text/css" href="results.css">\n')
            f.write('</head>\n')
            f.write('<body>\n')
            f.write(f"<h1>{student_info['Student name']}</h1>")
            f.write(f"<p>Student Code: {student_info['Student Code']}</p>")
            f.write(f"<p>Birthdate: {student_info['Birthdate']}</p>")
            f.write("<h2>Courses:</h2>")
            total_credits = 0
            total_points = 0
            grade_points = {'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
            for course_code, course_info in courses.items():
                filename = f"{course_code}.csv"
                if os.path.isfile(filename):
                    grades = read_csv(filename)
                    for row in grades:
                        if row["Student Code"] == student_info['Student Code']:
                            grade = row["Grade in Letters"]
                            credits = int(course_info['Credit Hours'])
                            f.write(f"<p>Course Code: {course_code}</p>")
                            f.write(f"<p>Course Name: {course_info['Course name']}</p>")
                            f.write(f"<p>Credit Hours: {credits}</p>")
                            f.write(f"<p>Grade: {grade}</p>")
                            f.write(f"<p>============</p>")
                            total_credits += credits
                            total_points += credits * grade_points[grade]
            gpa = total_points / total_credits if total_credits else 0
            f.write(f"<h2>Total Credit Hours: {total_credits}</h2>")
            f.write(f"<h2>GPA: {gpa:.2f}</h2>")
            f.write('</body>\n')
            f.write('</html>\n')
