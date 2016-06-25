import xml.etree.ElementTree as xml

def get_assignment_average(file_name, assignment_name):
    tree = xml.parse(file_name)
    root = tree.getroot()

    assignment_name = assignment_name.lower()
    totalscore = 0
    amount = 0
    points_possible = 0
    for assignment in root.iter('assignment'):
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


def list_assignments(file_name):  # Lists all assignments
    tree = xml.parse(file_name)
    root = tree.getroot()

    for all_assignments in root.iter('all_assignments'):
        for name in all_assignments.iter('name'):
            print(name.text)


def list_students(file_name):  # Lists all students
    tree = xml.parse(file_name)
    root = tree.getroot()

    for student in root.iter('student'):
        print(student.get('name'))


def parse_assignment(student):  # Formats/prints assignment info
    print("=======")
    print(student.get('name'))
    print("=======")
    totalposs = 0
    totalscore = 0

    for assignment in student.iter('assignment'):
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


def print_all_grades(file_name):  # Prints all grade profiles of all students
    tree = xml.parse(file_name)
    root = tree.getroot()

    for student in root.findall('student'):
        parse_assignment(student)


def one_student_grades(file_name, name):  # Prints grade profile of one student
    tree = xml.parse(file_name)
    root = tree.getroot()

    for student in root.findall('student'):
        x = student.get('name').lower()
        if x == name.lower():
            parse_assignment(student)
