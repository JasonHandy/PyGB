import xml.etree.ElementTree as xml
import os


def export(xmlfile):
    tree = xml.parse(xmlfile)
    root = tree.getroot()

    txtstring = ""
    buffer = "\n=======\n"
    output = "{!s} / {!s}	[{!s}%]"
    totalposs = 0
    totalscore = 0

    for student in root.findall('student'):
        txtstring += buffer + student.get('name') + buffer
        for assignment in student.findall('assignment'):
            txtstring += (">" + assignment.get('name'))
            poss = float(assignment.get('points_possible'))
            score = float(assignment.get('score'))
            perc = score / poss * 100

            totalposs += poss
            totalscore += score

            txtstring += ("\t" + output.format(score, poss, perc))
            txtstring += "\n"

        totalperc = totalscore / totalposs * 100
        txtstring += "\n\n> Total for {!s}".format(student.get('name'))
        txtstring += ("\t" + output.format(totalscore, totalposs, totalperc))

    destination = os.path.join(os.path.expanduser('~'), 'Desktop')

    with open(destination + '/GRADEBOOK.txt', 'w') as exportfile:
        exportfile.write(txtstring)

    print("Your file has been saved to your desktop!")
