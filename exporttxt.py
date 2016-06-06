import xml.etree.ElementTree as xml
import os

def init(xmlfile, writefile):
	global file
	file = xmlfile
	global tree
	tree = xml.parse(file)
	global root
	root = tree.getroot()
	export(writefile)
	
def export(txtfilename):
	txtstring = ""
	buffer = "\n=======\n"
	output = "{!s} / {!s}	[{!s}%]"
	totalposs = 0
	totalscore = 0
	
	for student in root.findall('student'):
		txtstring += buffer
		txtstring += student.get('name')
		txtstring += buffer
		for assignment in student.findall('assignment'):
			txtstring += (">" + assignment.find('name').text)
			poss = float(assignment.find('poss').text)
			score = float(assignment.find('score').text)
			perc = score / poss * 100
			
			totalposs += poss
			totalscore += score
			
			txtstring += ("\t" + output.format(score, poss, perc))
			txtstring += "\n"
		
		totalperc = totalscore / totalposs * 100
		txtstring += "\n\n> Total for {!s}".format(student.get('name'))
		txtstring += ("\t" + output.format(totalscore,totalposs,totalperc))
	
	txtfilename += ".txt"
	destination = os.path.join(os.path.expanduser('~'), 'Desktop', txtfilename)
	exportfile = open(destination, "w")
	exportfile.write(txtstring)
	exportfile.close()
	print("Your file has been saved to your desktop!")
	
