import mysql.connector as mysql


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Glassers1!",
    db = "School"
)

cursor = db.cursor()


def newStudent():
    firstName = input("Please enter first name: ")
    lastName = input("Please enter last name: ")
    query = ("INSERT INTO Student (first_name, last_name) VALUES (%s, %s)")
    values = {
        (firstName, lastName)
        }
    cursor.executemany(query,values)
    db.commit()
    
def newCourse():
    courseName = input("Enter course name ")
    courseDay = input("Enter day of course ")
    courseTime = input("Enter course time in format ##:## ")
    query = ("INSERT INTO Courses (course_name, course_day, course_time) VALUES (%s, %s, %s)")
    values = {
        (courseName, courseDay, courseTime)
        }
    cursor.executemany(query,values)
    db.commit()

def enrollCourse():
    studentId = input("Please enter your student id number: ")

    displayQuery = "SELECT * from Courses"
    cursor.execute(displayQuery)
    records = cursor.fetchall()

    print("\nCurrent Course Catalogue")
    for row in records:
        print("Course Id = ", row[0], )
        print("Course Name = ", row[1],)
        print("Course Day  = ", row[2],)
        print("Course Time  = ", row[3], "\n")


    courseId = input("Please enter course ID: ")
    query = ("INSERT INTO School.enroll_course (course_id, student_id) VALUES (%s, %s)")
    values = {
        (courseId, studentId)
        }
    cursor.executemany(query, values)
    db.commit()


def studentsEachCourse():

    courseId = input("Enter course id to view students in each course\n")

    
    cursor.execute("""SELECT s.student_id, first_name, last_name, course_name
                       FROM Student s JOIN enroll_course e ON s.student_id = e.student_id
		       JOIN Courses c ON c.course_id = e.course_id
                       WHERE c.course_id = %s""",(courseId,))
    records = cursor.fetchall()
    for row in records:
        print(row)
    print()


def coursesEachStudent():

    studentId = input("Enter student id to view all your courses\n")

    cursor.execute("""SELECT s.student_id, first_name, last_name, course_name
                        FROM Student s JOIN enroll_course e ON s.student_id = e.student_id
		        JOIN Courses c ON c.course_id = e.course_id
                        WHERE s.student_id = %s""",(studentId,))
    records = cursor.fetchall()
    for row in records:
        print(row)
    print()
    
def studentDaySchedule():

    studentId = input("Enter student id to view courses \n")
    day = input("Enter day of the week to view time of each course \n")

    cursor.execute("""SELECT s.student_id, first_name, last_name, course_name, course_day, course_time
                        FROM Student s JOIN enroll_course e ON s.student_id = e.student_id
			JOIN Courses c ON c.course_id = e.course_id
                        WHERE s.student_id = %s AND course_day = %s""",(studentId,day))
    records = cursor.fetchall()
    for row in records:
        print(row)
    print()
    
 
def main():
    print("Please select from the following options")
    option = input("[A] Enter New Student \n[B] Enter New Course " +
                   "\n[C] Enroll Course\n[D] Students In Each Course " +
                   "\n[E] Courses For Each Student\n[F] Course Schedule by Day\n[G] Quit\n" ).upper()
    
    while(option != "G"):
        if option == "A":
            newStudent()
        if option == "B":
            newCourse()
        if option == "C":
            enrollCourse()
        if option == "D":
            studentsEachCourse()
        if option == "E":
            coursesEachStudent()
        if option == "F":
            studentDaySchedule()
        if option == "G":
            break;
        option = input("[A] Enter New Student \n[B] Enter New Course " +
                   "\n[C] Enroll Course\n[D] Students In Each Course " +
                   "\n[E] Courses For Each Student\n[F] Course Schedule by Day\n[G] Quit\n" ).upper()
        
if __name__=="__main__":
    main()
