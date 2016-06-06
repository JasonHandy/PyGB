import xml.etree.ElementTree as xml

def init(filename):
	global file
	file = filename
	global tree
	tree = xml.parse(file)
	global root
	root = tree.getroot()
	
def get_average(work):
	work = work.lower()
	totalscore = 0
	amount = 0
	for assignment in root.iter('assignment'):
		if assignment.find('name').text.lower() == work:
			score = float(assignment.find('score').text)
			poss = float(assignment.find('poss').text)
			totalscore += score
			amount += 1
			
			print("\t>{!s}. {!s} [{!s}%]".format(amount, score, score/poss*100))
			print()
			
	average = totalscore / amount 
	percent = (average / poss) * 100
	print("The average for {!s} is {!s} [{!s}%]".format(work, average, percent))
	
def list_assignments():
	for allassign in root.iter('allassign'):
		for name in allassign.iter('name'):
			print(name.text)
		
		
def list_students():
	for student in root.iter('student'):
		print(student.get('name'))

def parse_assignment(student):
	print("=======") 
	print(student.get('name')) 
	print("=======")
	totalposs = 0
	totalscore = 0
	
	for assignment in student.findall('assignment'):
		name = assignment.find('name').text
		poss = assignment.find('poss').text
		score = assignment.find('score').text
		perc = (float(score) / float(poss)) * 100
		
		totalposs += float(poss)
		totalscore += float(score)
		
		print(">", name)
		output = "{!s} / {!s}    [{!s} %]" 
		print("\t", output.format(score,poss,perc))
		
	totalperc = (float(totalscore) / float(totalposs)) * 100
	print("> Total")
	print("\t", output.format(totalscore,totalposs,totalperc), "\n")

def print_all():
	for student in root.findall('student'): 
		parse_assignment(student)
def print_one(name):
	for student in root.findall('student'):
		x = student.get('name')
		if x == name:
			parse_assignment(student)


		