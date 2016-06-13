#!/usr/local/bin/python3
import tkinter as tk
from tkinter import filedialog
import exporttxt
import parse
import handler


def open_file():
    print("Please select the XML file containing your class data.\n")

    root = tk.Tk()  # Creates default tkinter window
    root.withdraw()  # Hides window from view
    root.update()  # Updates window to allow filedialog
    file_name = filedialog.askopenfilename()
    root.destroy()  # Destroys window after dialog

    if handler.is_file_type('xml', file_name):
        GRADEBOOK = file_name
        global GRADEBOOK
        parse.init(file_name)
        main_menu()
    else:
        print("Invalid file type. Please choose another.")
        open_file()


def new_file():
    file_name = input("What would you like to name this gradebook? ")
    file_name += '.xml'


def main_menu():
    print("\nYou are using the file {!s}\n".format(GRADEBOOK))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] View grades.")
    print("\t[2] Edit grades.")  # TO DO
    print("\t[3] File options for {!s}.".format(GRADEBOOK))
    print("\t[4] Quit.")

    choice = input("> ")

    if choice == '1':
        view_menu()
    elif choice == '2':
        edit_menu()
    elif choice == '3':
        file_menu()
    elif choice == '4':
        quit()
    else:
        print("Invalid selection.")
        main_menu()


def view_menu():
    end_prompt = "Press any key to continue"
    print("\nYou are using the file {!s}\n".format(GRADEBOOK))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] View class report.")
    print("\t[2] View student report.")
    print("\t[3] View class statistics.")
    print("\t[4] Back to main menu.")

    choice = input("> ")

    if choice == '1':
        parse.print_all_grades()
        input(end_prompt)
        view_menu()

    elif choice == '2':
        print("List of students:\n")
        parse.list_students()
        print("\nEnter the name of a student, then press RETURN.")
        name = input("> \n")

        if handler.is_a_student(name, GRADEBOOK):
            parse.one_student_grades(name)
            input(end_prompt)
            view_menu()
        else:
            print("{!s} is not a student. Press RETURN to go back to"
                  " menu.".format(name))
            input("")
            view_menu()

    elif choice == '3':
        pass
        # TO DO

    elif choice == '4':
        main_menu()
    else:
        print("Invalid selection.")
        view_menu()

def edit_menu():
    print()
    # TO DO


def file_menu():
    end_prompt = "Press any key to continue"
    print("\nYou are using the file {!s}\n".format(GRADEBOOK))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] Export gradebook to text file.")
    print("\t[2] Open gradebook file.")  # TO DO
    print("\t[3] Create new gradebook")  # TO DO
    print("\t[4] Back to main menu.")  # TO DO

    choice = input("> ")

    if choice == '1':
        exporttxt.export(GRADEBOOK)
        input(end_prompt)
        view_menu()

    elif choice == '2':
        open_file()

    elif choice == '3':
        new_file()


print("\n\n\n")
print("Welcome to SimpleGrade version {!s}!\n".format('0.2'))
op = input("Would you like to [O]pen and existing file, or create a [N]ew "
           "one?\n")

if op == 'O':
    open_file()
elif op =='N':
    new_file()
