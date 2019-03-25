'''
Name: Jarron Bailey
Date: 02/18/19
Homework 4

'''

import csv
import os
from pathlib import Path


def createHtmlDoc():
    '''Create HTML file with users name and description'''

    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    f = open("index.html", "w")
    htmlDoc = [
        "<!DOCTYPE html>" + "\n",
        '<html lang="en">' + "\n",
        "" + "\n",
        "<head>" + "\n",
        ' <meta charset="UTF-8">' + "\n",
        ' <meta name="viewport" content="width=device-width, initial-scale=1.0">' + "\n",
        ' <meta http-equiv="X-UA-Compatible" content="ie=edge">' + "\n",
        ' <title>Homework 4</title>' + "\n",
        "</head>" + "\n",
        "<body>" + "\n",
        '<h1 style="text-align: center">' + name + '</h1>' + "\n",
        "<hr />" + "\n",
        '<p>' + description + '</p>' + "\n",
        "<hr />" + "\n",
        "</body>" + "\n",
        "" + "\n",
        "</html>" + "\n"
    ]

    f.writelines(htmlDoc)
    f.close()


def csvIntoList():
    '''Read CSV and turn into a formated array of all students [[ID, Name, Course, Course Hours, Course Grade], ...]'''

    formattedStudentReport = []
    fh = open("students-information.csv", "r")
    studentsReports = fh.readlines()
    _aux = 0
    ctr = 0
    while _aux < len(studentsReports):
        studentName = ""
        formattedRow = ""
        studentID = studentsReports[_aux].split(",")[0]
        studentName += (studentsReports[_aux].split(",")[1].replace('"', ""))
        studentName += studentsReports[_aux].split(",")[2].replace('"', "")
        studentCourse = studentsReports[_aux].split(",")[3]
        courseCredits = studentsReports[_aux].split(",")[4]
        courseGrade = studentsReports[_aux].split(",")[5].replace('\n', "")
        formattedRow += studentID + "," + studentName + "," + \
            studentCourse + "," + courseCredits + "," + courseGrade
        formattedStudentReport.append(formattedRow)
        _aux += 1
    formattedArray = []
    while ctr < len(formattedStudentReport):
        row = formattedStudentReport[ctr].split(",")
        formattedArray.append(row)
        ctr += 1
    return formattedArray


def filterStudent(id, filteredStudentArray):
    '''Takes for formmatted array and return an array with rows containg student with ID'''
    filteredArray = list(filter(lambda x: x[0] == id, filteredStudentArray))
    return filteredArray


def gradeLetterToNum(grade):
    '''Takes letter grade and return the numerical value of the letter'''
    if grade == "A":
        grade = 4
        return grade
    if grade == "B":
        grade = 3
        return grade
    if grade == "C":
        grade = 2
        return grade
    if grade == "D":
        grade = 1
        return grade
    if grade == "F":
        grade = 0
        return grade


def gpaCalculator(filteredStudentArray):
    '''Takes the student array and return the calulated gpa'''
    numCredits = 0
    gradePoints = 0
    ctr = 0
    while ctr < len(filteredStudentArray):
        gradePoints += int(filteredStudentArray[ctr][3]) * \
            gradeLetterToNum(filteredStudentArray[ctr][4])
        numCredits += int(filteredStudentArray[ctr][3])
        ctr += 1

    return gradePoints/numCredits


def createStudentFile(filteredStudentArray):
    '''Loops through each ID and creates and outputs a new file in the "student-reports" folder" '''
    ctr = 0
    ctr2 = 0
    studentName = filteredStudentArray[ctr][1]
    ID = filteredStudentArray[ctr][0]
    courses = []
    courseCredits = []
    courseGrade = []
    sumOfCredits = 0
    gpa = float("{0:.2f}".format(gpaCalculator(filteredStudentArray)))
    tabsBtwnCodeAndCreds = "\t\t\t\t\t\t\t\t\t\t"
    tabsBtwnCredsAndGrade = "\t\t\t\t\t\t\t\t\t\t\t"

    my_file = Path("./student-reports/" + studentName + "Report.txt")
    if my_file.is_file():
        os.remove(my_file)

    while ctr < len(filteredStudentArray):
        courses.append(filteredStudentArray[ctr][2])
        courseCredits.append(filteredStudentArray[ctr][3])
        sumOfCredits += int(filteredStudentArray[ctr][3])
        courseGrade.append(filteredStudentArray[ctr][4])
        ctr += 1

    '''Generates header for each student'''
    studentHeader = [
        'Student Name: ' + studentName + "\n",
        'Student ID Number: ' + ID + "\n",
        "\n",
        "Course Code" + "\t\t\t\t" + "Course Credits" +
        "\t\t\t\t" + "Course Grade" + "\n",
        "_____________________________________________________" + "\n",
    ]

    with open("./student-reports/" + studentName + "Report.txt", "a") as myfile:
        myfile.writelines(studentHeader)

    '''Generates course listings for each student'''
    while ctr2 < len(filteredStudentArray):
        row = [courses[ctr2] + tabsBtwnCodeAndCreds +
               courseCredits[ctr2] + tabsBtwnCredsAndGrade + courseGrade[ctr2] + "\n"]
        with open("./student-reports/" + studentName + "Report.txt", "a") as myfile:
            myfile.writelines(row)
        ctr2 += 1

    '''Generates footer for each student'''
    footer = [
        "\n",
        'Total Semester Course Credits Completed: ' + str(sumOfCredits) + "\n",
        'Semester GPA: ' + str(gpa) + "\n",
    ]

    with open("./student-reports/" + studentName + "Report.txt", "a") as myfile:
        myfile.writelines(footer)


def main():
    '''Runs HTML program '''
    createHtmlDoc()

    '''Runs program for each student in the formated student report '''
    formattedStudentReport = csvIntoList()
    ctr = 0
    if not os.path.exists("./student-reports"):
        os.makedirs("./student-reports")
    while ctr < len(formattedStudentReport):
        ID = formattedStudentReport[ctr][0]
        filteredStudentArray = filterStudent(ID, formattedStudentReport)
        gpa = gpaCalculator(filteredStudentArray)
        createStudentFile(filteredStudentArray)
        ctr += 1
    print("Students reports can be found in the `student-reports` directory")


main()
