import xml.etree.ElementTree as Xml
import os


def get_statistics(file_name):
    output_string = ""

    output_string += "\n======\n"
    output_string += "ASSIGNMENT AVERAGES\n"
    output_string += "======\n"
    output_string += each_assignment_average(file_name) + "\n"

    print(output_string)

    print("Type [text] to export this to a text file. Press any other key to "
          "return to the menu")
    text_choice = str(input("> "))

    if text_choice.lower() == 'text':
        destination = os.path.join(os.path.expanduser('~'), 'Desktop')
        with open(destination + "/CLASS_STATS.txt", 'w+') as file:
            file.write(output_string)
            print("File created!")
    else:
        pass


def each_assignment_average(file_name):
    tree = Xml.parse(file_name)
    root = tree.getroot()
    return_string = ""

    for all_assignment in root.find('all_assignments'):
        # Get assignment name and set average
        assignment_name = all_assignment.text
        total_score = 0
        count = 0
        # Get assignment from each student, and add to average
        for student in root.iter('student'):
            for student_assignment in student.iter('assignment'):
                if student_assignment.get('name') == assignment_name:
                    count += 1
                    total_score += float(student_assignment.get('score'))
        # Calculate total points possible, and find average
        points_possible = float(all_assignment.get('points_possible')) * count
        average = total_score / count
        percent = (total_score / points_possible) * 100

        return_string += "Name: {!s}\t\tAvg: {!s} / {!s}pts [{!s}%]\n".format(
            assignment_name, average, all_assignment.get('points_possible'),
            percent)
    return return_string
