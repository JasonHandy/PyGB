import xml.etree.ElementTree as xml


def init(filename):
    tree = xml.parse(filename)
    ROOT = tree.getroot()
    global ROOT


def get_assignment_average(assignment_name):
    assignment_name = assignment_name.lower()
    totalscore = 0
    amount = 0
    points_possible = 0
    for assignment in ROOT.iter('assignment'):
        if assignment.get('name').lower() == assignment_name:
            score = float(assignment.get('score'))
            points_possible = float(assignment.get('points_possible'))
            totalscore += score
            amount += 1

            print("\t>{!s}. {!s} [{!s}%]".format(amount, score,
                                                 score / points_possible * 100))
            print()

    average = totalscore / amount
    percent = (average / points_possible) * 100
    print("The average for {!s} is {!s} [{!s}%]".format(assignment_name,
                                                        average, percent))


def list_assignments():  # Lists all assignments
    for allassign in ROOT.iter('allassign'):
        for name in allassign.iter('name'):
            print(name.text)


def list_students():  # Lists all students
    for student in ROOT.iter('student'):
        print(student.get('name'))


def parse_assignment(student):  # Gets, formats, and prints assignment info
    print("=======")
    print(student.get('name'))
    print("=======")
    totalposs = 0
    totalscore = 0

    for assignment in student.findall('assignment'):
        name = assignment.get('name')
        points_possible = assignment.get('points_possible')
        score = assignment.get('score')
        perc = (float(score) / float(points_possible)) * 100

        totalposs += float(points_possible)
        totalscore += float(score)

        print(">", name)
        output = "{!s} / {!s}    [{!s} %]"
        print("\t", output.format(score, points_possible, perc))

    totalperc = (float(totalscore) / float(totalposs)) * 100
    print("> Total")
    print("\t", output.format(totalscore, totalposs, totalperc), "\n")


def print_all_grades():  # Prints all grade profiles of all students
    for student in ROOT.findall('student'):
        parse_assignment(student)


def one_student_grades(name):  # Prints the grade profile of one student
    for student in ROOT.findall('student'):
        x = student.get('name').lower()
        if x == name:
            parse_assignment(student)
