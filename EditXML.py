import xml.etree.ElementTree as Xml
import os


def create_new_gradebook(file_name):
    with open(file_name, 'w+'):
        print("Gradebook created!")

    root = Xml.Element('Gradebook')
    tree = Xml.ElementTree(root)
    Xml.SubElement(root, 'all_assignments')
    tree.write(file_name)


def delete_gradebook(file_name):
    try:
        os.remove(file_name)
        print("\nGradebook deleted.")
    except FileNotFoundError:
        print("\nThat file does not exist.")


def make_pretty(file_name):
    from xml.dom import minidom

    # Open ugly XML file
    with open(file_name, "r") as gradebook:
        # Get string from ugly XML file
        file_string = gradebook.read()

        # Turn ugly XML into pretty XML
        formatted_string = minidom.parseString(file_string).toprettyxml()

    # Re-open and truncate ugly XML file
    with open(file_name, "w+") as formatted_gradebook:
        # Write pretty XML to file and close
        formatted_gradebook.write(formatted_string)

    print("{!s} was made into pretty XML!".format(file_name))


def add_student(file_name):
    tree = Xml.parse(file_name)
    root = tree.getroot()

    student_name = str(input("Enter student name: "))
    Xml.SubElement(root, 'student', attrib={'name': student_name})
    tree.write(file_name)

    print("\nType [quit] to stop entering names and go to the menu.\n")
    print("\nPress RETURN to continue entering names.")

    choice = str(input("> "))

    if choice.lower() == 'quit':
        pass
    else:
        add_student(file_name)


def add_assignment(file_name):
    # Add assignments to <all_assignments> block
    tree = Xml.parse(file_name)
    root = tree.getroot()

    all_assignments = root.find('all_assignments')
    assignment_name = str(input("Enter assignment name: "))
    points_possible = str(input("How many points is {!s} worth?".format(
        assignment_name)))

    Xml.SubElement(all_assignments, 'name', attrib={
        "points_possible": points_possible}).text = assignment_name
    tree.write(file_name)

    # Add assignments to <student> blocks
    tree = Xml.parse(file_name)
    root = tree.getroot()

    for student in root.iter('student'):
        student_name = student.get('name')
        score = str(input("What did {!s} get on {!s}?".format(student_name,
                                                              assignment_name)))
        try: # TODO: YOU ARE HERE!!!
            percent = (float(score) / float(points_possible)) * 100
        except ZeroDivisionError:
            percent = None

        Xml.SubElement(student, 'assignment', attrib={'name': assignment_name,
                                                      'points_possible':
                                                          points_possible,
                                                      'score': score,
                                                      'percent': str(percent)})
        tree.write(file_name)

    print("\nType [quit] to stop entering assignments and go to the menu.\n")
    print("\nPress RETURN to continue entering assignments.")

    choice = str(input("> "))

    if choice.lower() == 'quit':
        pass
    else:
        add_assignment(file_name)
