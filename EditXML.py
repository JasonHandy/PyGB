import xml.etree.ElementTree as xml

# TODO (CREATE DISTINCTION BETWEEN ADDING FIRST TIME AND OTHER TIMES)

def initialize_new_file(file_name):
    with open(file_name):
        print("Gradebook created!")

    root = xml.Element('Data')
    tree = xml.ElementTree(root)
    xml.SubElement(root, 'allassign')
    tree.write(file_name)


def add_students(file_name):
    tree = xml.parse(file_name)
    root = tree.getroot()

    student_name = str(input("Enter student name: "))
    xml.SubElement(root, 'student', attrib={'name': student_name})
    tree.write(file_name)

    print("\n[1]Enter another student.")
    print("\n[2]Enter assignments.")
    print("\n[3]Main Menu.")

    choice = input('> ')

    if choice == '1':
        add_students(file_name)
    elif choice == '2':
        add_assignments(file_name)
    elif choice == '3':
        pass


def add_assignments(file_name):
    # Add assignments to <allassign> block
    tree = xml.parse(file_name)
    root = tree.getroot()

    allassign = root.find('allassign')
    assignment_name = str(input("Enter assignment name: "))
    points_possible = str(input("How many points is {!s} worth? ".format(
        assignment_name)))

    xml.SubElement(allassign, 'name').text = assignment_name
    tree.write(file_name)

    # Add assignments to each student block
    for student in root.iter('student'):
        xml.SubElement(student, 'assignment', attrib={'name': assignment_name,
                                                      'points_possible':
                                                      points_possible})
        tree.write(file_name)

    print("\n[1]Enter another assignment.")
    print("\n[2]Enter grades.")
    print("\n[3]Main Menu.")

    choice = input('> ')

    if choice == '1':
        add_assignments(file_name)
    elif choice == '2':
        add_grades(file_name)
    elif choice == '3':
        pass


def add_grades(file_name):
    tree = xml.parse(file_name)
    root = tree.getroot()

    for student in root.iter('student'):
        student_name = student.get('name')

        for assignment in student.iter('assignment'):
            assignment_name = assignment.get('name')

            score = str(input("What did {!s} get on {!s}? ".format(
                student_name, assignment_name)))
            assignment.set('score', score)
            tree.write(file_name)

    pass

