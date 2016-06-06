#!/usr/local/bin/python3
import tkinter as tk
from tkinter import filedialog
import exporttxt, info, parse

def change_file():
	print("Please select the XML file containing your class data.\n")
	global filename
	root = tk.Tk()
	root.withdraw()
	root.update()
	filename = filedialog.askopenfilename()
	root.destroy()
	parse.init(filename)
	main_menu()
	
def main_menu():
	goback = "Press <RETURN> go to back to the menu. "

	print("\nYou are using the file {!s}\n".format(filename))
	print("Choose an option by typing the number and pressing <RETURN>: ")
	print("\t[1] View all grades.")
	print("\t[2] View grades from one student.")
	print("\t[3] View class average.")
	print("\t[4] Export XML gradebook to text file.")
	print("\t[5] List assignments.")
	print("\t[6] List students.")
	print("\t[7] About this program.")
	print("\t[8] Quit.")
	
	choice = int(input("> ")) #ERROR
	
	if choice in range(1,9):
		if choice == 1:
			parse.print_all()
			input(goback)
			main_menu()
		elif choice == 2:
			name = input("Please enter the name of the student: ")
			parse.print_one(name)
			input(goback)
			main_menu()
		elif choice == 3:
			assignment = input("Please enter the name of the assignment: ")
			parse.get_average(assignment)
			input(goback)
			main_menu()
		elif choice == 4:
			exporttxt.init(filename)
		elif choice == 5:
			parse.list_assignments()
			input(goback)
			main_menu()
		elif choice == 6:
			parse.list_students()
			input(goback)
			main_menu()
		elif choice == 7:
			info.version()
			info.about()
			input(goback)
			main_menu()
		elif choice == 8:
			quit()
	else:
		print("\n\nInvalid response, please try again.\n")
		main_menu()






print("\n\n\n")
print("Welcome to SimpleGrade version {!s}!\n".format(info.version()))
input("Press <RETURN> to continue.\n")
change_file()