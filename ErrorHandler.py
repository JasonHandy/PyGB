# This module exists to handle possible errors arising from user input.
import xml.etree.ElementTree as Xml


def is_a_student(name, path):
    tree = Xml.parse(path)
    root = tree.getroot()

    for student in root.iter('student'):
        if name.lower() == student.get('name').lower():
            return True
    return False


def is_an_assignment(name, path):
    tree = Xml.parse(path)
    root = tree.getroot()

    for assignment in root.iter('assignment'):
        if name.lower() == assignment.find('name').text.lower():
            return True
    return False
