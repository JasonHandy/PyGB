import xml.etree.ElementTree as Xml
import os


def export(xml_file):
    tree = Xml.parse(xml_file)
    root = tree.getroot()

    text_string = ""
    buffer = "\n=======\n"
    output = "{!s} / {!s}	[{!s}%]"
    total_possible = 0
    total_score = 0

    for student in root.findall('student'):
        text_string += buffer + student.get('name') + buffer
        for assignment in student.findall('assignment'):
            text_string += (">" + assignment.get('name'))
            poss = float(assignment.get('points_possible'))
            score = float(assignment.get('score'))
            percent = score / poss * 100

            total_possible += poss
            total_score += score

            text_string += ("\t" + output.format(score, poss, percent))
            text_string += "\n"

        total_percent = total_score / total_possible * 100
        text_string += "\n\n> Total for {!s}".format(student.get('name'))
        text_string += ("\t" + output.format(total_score, total_possible,
                                             total_percent))

    destination = os.path.join(os.path.expanduser('~'), 'Desktop')

    with open(destination + '/GRADEBOOK.txt', 'w') as export_file:
        export_file.write(text_string)

    print("Your file has been saved to your desktop!")
