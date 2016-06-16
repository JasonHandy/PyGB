#!/usr/local/bin/python3
import os
import ExportXML
import ParseXML
import EditXML
import ErrorHandler

# TODO(SWITCH TO APPLICATIONS DIRECTORY [/Applications])
save_path = os.path.join('/Volumes', 'HDD', 'PyGB-0.3-alpha', 'Gradebooks')


def open_file():
    print("\nPlease select the XML file containing your class data.\n")

    gradebook_list = os.listdir(save_path)
    for gradebook in gradebook_list:
        print('\t>', gradebook.replace('.xml', ''), '\n')
        
    FILE_NAME = os.path.join(save_path, str(input("> ")) + '.xml')

    if ErrorHandler.is_file_type('xml', FILE_NAME):
        ParseXML.init(FILE_NAME)
        global FILE_NAME
        main_menu()
    else:
        print("\nInvalid file type. Please choose another.")
        open_file()


def new_file():
    gradebook_name = str(input("What would you like to name this gradebook? "))
    FILE_NAME = os.path.join(save_path, gradebook_name + '.xml')

    with open(FILE_NAME, 'w'):
        print("{!s} gradebook created!".format(FILE_NAME))

    EditXML.initialize_new_file(FILE_NAME)
    EditXML.add_students(FILE_NAME)

    ParseXML.init(FILE_NAME)

    global FILE_NAME
    main_menu()


def main_menu():
    print("\nYou are using the file {!s}\n".format(FILE_NAME))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] View grades.")
    print("\t[2] Edit grades.")  # TODO (Create functionality to edit grades)
    print("\t[3] File options for {!s}.".format(FILE_NAME))
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
    print("\nYou are using the file {!s}\n".format(FILE_NAME))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] View class report.")
    print("\t[2] View student report.")
    print("\t[3] View class statistics.")
    print("\t[4] Back to main menu.")

    choice = input("> ")

    if choice == '1':
        ParseXML.print_all_grades()
        input(end_prompt)
        view_menu()

    elif choice == '2':
        print("List of students:\n")
        ParseXML.list_students()
        print("\nEnter the name of a student, then press RETURN.")
        name = input("> \n")

        if ErrorHandler.is_a_student(name, FILE_NAME):
            ParseXML.one_student_grades(name)
            input(end_prompt)
            view_menu()
        else:
            print("{!s} is not a student. Press RETURN to go back to"
                  " menu.".format(name))
            input("")
            view_menu()

    elif choice == '3':
        pass
        # TODO (CREATE STATISTICS)

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
    print("\nYou are using the file {!s}\n".format(FILE_NAME))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] Export gradebook to text file.")
    print("\t[2] Open gradebook file.")
    print("\t[3] Create new gradebook")
    print("\t[4] Back to main menu.")  # TO DO

    choice = input("> ")

    if choice == '1':
        ExportXML.export(FILE_NAME)
        input(end_prompt)
        view_menu()

    elif choice == '2':
        open_file()

    elif choice == '3':
        new_file()

    elif choice == '4':
        main_menu()


print("\n\n\n")
print("Welcome to SimpleGrade version {!s}!\n".format('0.2'))
op = input("Would you like to [O]pen an existing file, or create a [N]ew "
           "one?\n")

if op.lower() == 'o':
    open_file()
elif op.lower() == 'n':
    new_file()
