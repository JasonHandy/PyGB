import xml.etree.ElementTree as Xml

# TODO: CALCULATE PERCENTAGES DURING XML CREATING

def get_assignment_average(file_name, assignment_name):
    tree = Xml.parse(file_name)
    root = tree.getroot()

    # Initialize module variables. Vars set to 0 have error handling set up
    assignment_name = assignment_name.lower()
    total_score = 0
    amount = 0
    points_possible = 0

    for assignment in root.iter('assignment'):
        #  Iterate through assignments until one matches the request
        if assignment.get('name').lower() == assignment_name:
            score = float(assignment.get('score'))
            points_possible = float(assignment.get('points_possible'))
            total_score += score
            amount += 1
            try:
                print("\t>{!s}. {!s} [{!s}%]\n".format(amount, score,
                                                       score / points_possible *
                                                       100))
            except ZeroDivisionError:
                print("Zero Division Error! The points possible for "
                      "assignment {!s} are not "
                      "assigned, make sure to assign these before calculating "
                      "the grade!".format(assignment_name))
    try:
        average = total_score / amount
        percent = (average / points_possible) * 100
        print("The average for {!s} is {!s} [{!s}%]".format(assignment_name,
                                                            average, percent))
    except ZeroDivisionError:
        print("Zero Division Error! There are no points possible for any "
              "assignment. Make sure to assign points before calculating the "
              "grade!")


def list_assignments(file_name):  # Lists all assignments
    tree = Xml.parse(file_name)
    root = tree.getroot()

    for all_assignments in root.iter('all_assignments'):
        for name in all_assignments.iter('name'):
            print(name.text)


def list_students(file_name):  # Lists all students
    tree = Xml.parse(file_name)
    root = tree.getroot()

    for student in root.iter('student'):
        print(student.get('name'))


def parse_assignment(student):  # Formats & prints assignment info
    print("=======")
    print(student.get('name'))
    print("=======")

    # Initialize module variables. Vars set to 0 have error handling set up.
    total_poss = 0
    total_score = 0

    for assignment in student.iter('assignment'):
        assignment_name = assignment.get('name')
        points_possible = assignment.get('points_possible')
        score = assignment.get('score')
        percent = float(assignment.get('percent'))

        total_poss += float(points_possible)
        total_score += float(score)

        print(">", assignment_name)
        output = "{!s} / {!s}    [{!s} %]"
        print("\t", output.format(score, points_possible, percent))
    try:
        total_percent = (float(total_score) / float(total_poss)) * 100
        print("> Total")
        print("\t\t", output.format(total_score, total_poss, total_percent),
              "\n")
    except ZeroDivisionError:
        print("Zero Division Error! {!s} does not have points assigned to "
              "their assignments".format(student.get('name')))


def print_all_grades(file_name):  # Prints all grade profiles of all students
    tree = Xml.parse(file_name)
    root = tree.getroot()

    total_students = 0
    for student in root.findall('student'):
        total_students += 1
    if total_students != 0:
        for student in root.findall('student'):
            parse_assignment(student)
    else:
        print("There are no students in this gradebook!")


def one_student_grades(file_name, name):  # Prints grade profile of one student
    tree = Xml.parse(file_name)
    root = tree.getroot()

    for student in root.findall('student'):
        x = student.get('name').lower()
        if x == name.lower():
            parse_assignment(student)
