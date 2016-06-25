import xml.etree.ElementTree as xml
import os


def create_new_gradebook(file_name):
    with open(file_name, 'w+') as file:
        print("Gradebook created!")

    root = xml.Element('Gradebook')
    tree = xml.ElementTree(root)
    xml.SubElement(root, 'all_assignments')
    tree.write(file_name)


def delete_gradebook(file_name):
    os.remove(file_name)
    print("\nGradebook deleted.")


def make_pretty(file_name):
    from xml.dom import minidom

    with open(file_name, "r") as gradebook:
        file_string = gradebook.read()

        formatted_string = minidom.parseString(file_string).toprettyxml()

    with open(file_name, "w+") as formatted_gradebook:
        formatted_gradebook.write(formatted_string)


def add_student(file_name):
    tree = xml.parse(file_name)
    root = tree.getroot()

    student_name = str(input("Enter student name: "))
    xml.SubElement(root, 'student', attrib={'name': student_name})
    tree.write(file_name)

    print("\nType [quit] to stop entering names and go to the menu.\n")
    print("\nPress RETURN to continue entering names.")

    choice = input("> ")

    if choice.lower() == 'quit':
        pass
    else:
        add_student(file_name)


def add_assignment(file_name):
    # Add assignments to <all_assignments> block
    tree = xml.parse(file_name)
    root = tree.getroot()

    all_assignments = root.find('all_assignments')
    assignment_name = str(input("Enter assignment name: "))
    points_possible = str(input("How many points is {!s} worth?".format(
        assignment_name)))

    xml.SubElement(all_assignments, 'name', attrib={
        "points_possible":points_possible}).text = assignment_name
    tree.write(file_name)

    # Add assignments to <student> blocks
    tree = xml.parse(file_name)
    root = tree.getroot()

    for student in root.iter('student'):
        student_name = student.get('name')
        score = str(input("What did {!s} get on {!s}?".format(student_name,
                                                              assignment_name)))

        xml.SubElement(student, 'assignment', attrib={'name':assignment_name,
                                                      'points_possible':
                                                          points_possible,
                                                      'score': score})
        tree.write(file_name)


    print("\nType [quit] to stop entering assignments and go to the menu.\n")
    print("\nPress RETURN to continue entering assignments.")

    choice = input("> ")

    if choice.lower() == 'quit':
        pass
    else:
        add_assignment(file_name)
